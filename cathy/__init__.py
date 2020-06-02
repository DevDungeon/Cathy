import aiml
from datetime import datetime, timedelta
import discord
import os
import pkg_resources
import logging
import sqlite3
from signal import signal, SIGINT, SIGTERM
from sys import exit


logging.basicConfig(level=logging.INFO)


class Cathy:

    STARTUP_FILE = "std-startup.xml"
    SQL_SCHEMA = [
        'CREATE TABLE IF NOT EXISTS chat_log (time, server_name, user_id, message, response)',
        'CREATE TABLE IF NOT EXISTS users (id, name, first_seen)',
        'CREATE TABLE IF NOT EXISTS servers (id, name, first_seen)',
    ]

    def exit_handler(signal_received, frame):
        logging.info(f"[*] Signal received ({signal_received})....Exiting.")
        exit()

    def __init__(self, channel_name, bot_token, database):
        """
        Initialize the bot using the Discord token and channel name to chat in.

        :param channel_name: Only chats in this channel. No hashtag included.
        :param bot_token: Full secret bot token
        :param database: Path for sqlite file to use
        """
        # Store configuration values
        self.channel_name = channel_name
        self.token = bot_token
        self.database = database
        self.message_count = 0
        self.last_reset_time = datetime.now()

        logging.info("[*] Setting up signal handlers")
        signal(SIGINT, self.exit_handler)
        signal(SIGTERM, self.exit_handler)

        # Setup database
        logging.info("[*] Initializing database...")
        self.db = sqlite3.connect(self.database)
        self.cursor = self.db.cursor()
        self.setup_database_schema()
        logging.info('[+] Database initialized')

        # Load AIML kernel
        logging.info("[*] Initializing AIML kernel...")
        start_time = datetime.now()
        self.aiml_kernel = aiml.Kernel()
        self.setup_aiml()
        end_time = datetime.now()
        logging.info(f"[+] Done initializing AIML kernel. Took {end_time - start_time}")

        # Set up Discord
        logging.info("[*] Initializing Discord bot...")
        self.discord_bot = discord.AutoShardedClient()
        self.setup_discord_events()
        logging.info("[+] Done initializing Discord bot.")
        logging.info("[+] Exiting __init__ function.")

    def setup_database_schema(self):
        for sql_statement in self.SQL_SCHEMA:
            self.cursor.execute(sql_statement)
        self.db.commit()

    def setup_aiml(self):
        initial_dir = os.getcwd()
        os.chdir(pkg_resources.resource_filename(__name__, ''))  # Change directories to load AIML files properly
        startup_filename = pkg_resources.resource_filename(__name__, self.STARTUP_FILE)
        self.aiml_kernel.setBotPredicate("name", "Cathy")
        self.aiml_kernel.learn(startup_filename)
        self.aiml_kernel.respond("LOAD AIML B")
        os.chdir(initial_dir)

    async def reset(self, message):
        """
        Allow users to trigger a cathy reset up to once per hour. This can help when the bot quits responding.
        :return:
        """
        now = datetime.now()
        if datetime.now() - self.last_reset_time > timedelta(hours=1):
            self.last_reset_time = now
            await message.channel.send('Resetting my brain...')
            self.aiml_kernel.resetBrain()
            self.setup_aiml()
        else:
            await message.channel.send(
                f'Sorry, I can only reset once per hour and I was last reset on {self.last_reset_time} UTC')

    def setup_discord_events(self):
        """
        This method defines all of the bot command and hook callbacks
        :return:
        """
        logging.info("[+] Setting up Discord events")

        @self.discord_bot.event
        async def on_ready():
            logging.info("[+] Bot on_ready even fired. Connected to Discord")
            logging.info("[*] Name: {}".format(self.discord_bot.user.name))
            logging.info("[*] ID: {}".format(self.discord_bot.user.id))

        @self.discord_bot.event
        async def on_message(message):
            self.message_count += 1

            if message.author.bot or str(message.channel) != self.channel_name:
                return

            if message.content is None:
                logging.error("[-] Empty message received.")
                return

            if message.content.startswith('!reset'):
                await self.reset(message)
                return

            # Clean out the message to prevent issues
            text = message.content
            for ch in ['/', "'", ".", "\\", "(", ")", '"', '\n', '@', '<', '>']:
                text = text.replace(ch, '')

            try:
                aiml_response = self.aiml_kernel.respond(text)
                aiml_response = aiml_response.replace("://", "")
                aiml_response = aiml_response.replace("@", "")  # Prevent tagging and links
                aiml_response = "`@%s`: %s" % (message.author.name, aiml_response)  # Remove unicode to prevent errors

                if len(aiml_response) > 1800:  # Protect against discord message limit of 2000 chars
                    aiml_response = aiml_response[0:1800]

                now = datetime.now()
                self.insert_chat_log(now, message, aiml_response)

                await message.channel.send(aiml_response)

            except discord.HTTPException as e:
                logging.error("[-] Discord HTTP Error: %s" % e)
            except Exception as e:
                logging.error("[-] General Error: %s" % e)

    def run(self):
        logging.info("[*] Now calling run()")
        self.discord_bot.run(self.token)
        logging.info("[*] Bot finished running.")

    def insert_chat_log(self, now, message, aiml_response):
        self.cursor.execute('INSERT INTO chat_log VALUES (?, ?, ?, ?, ?)',
                            (now.isoformat(), message.guild.id, message.author.id,
                             str(message.content), aiml_response))

        # Add user if necessary
        self.cursor.execute('SELECT id FROM users WHERE id=?', (message.author.id,))
        if not self.cursor.fetchone():
            self.cursor.execute(
                'INSERT INTO users VALUES (?, ?, ?)',
                (message.author.id, message.author.name, datetime.now().isoformat()))

        # Add server if necessary
        self.cursor.execute('SELECT id FROM servers WHERE id=?', (message.guild.id,))
        if not self.cursor.fetchone():
            self.cursor.execute(
                'INSERT INTO servers VALUES (?, ?, ?)',
                (message.guild.id, message.guild.name, datetime.now().isoformat()))

        self.db.commit()

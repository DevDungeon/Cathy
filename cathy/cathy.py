"""
Cathy AI Discord Chat Bot

Written in Python 3 using AIML chat library.
"""
import aiml
import asyncio
from datetime import datetime, timedelta
import discord
import os
import pkg_resources
import random
from discord.ext import commands
import logging
import logging.config
import sqlite3
from signal import signal, SIGINT, SIGTERM
from sys import exit


class ChattyCathy:

    STARTUP_FILE = "std-startup.xml"
    BOT_PREFIX = ('?', '!')
    SQL_SCHEMA = [
        'CREATE TABLE IF NOT EXISTS chat_log (time, server_name, user_id, message, response)',
        'CREATE TABLE IF NOT EXISTS users (id, name, first_seen)',
        'CREATE TABLE IF NOT EXISTS servers (id, name, first_seen)',
    ]

    def exit_handler(signal_received, frame):
        self.logger.info(f"[*] Signal received ({signal_received})....Exiting.")
        exit()

    def __init__(self, channel_name, bot_token, log_file, database):
        """
        Initialize the bot using the Discord token and channel name to chat in.

        :param channel_name: Only chats in this channel. No hashtag included.
        :param bot_token: Full secret bot token
        :param log_file: File for logging details
        :param database: Path for sqlite file to use
        """
        # Store configuration values
        self.channel_name = channel_name
        self.token = bot_token
        self.log_file = log_file
        self.database = database
        self.message_count  = 0
        self.last_reset_time = datetime.now()

        # Log configuration
        self.logger = logging.getLogger('cathy_logger')
        self.setup_logging()
        self.logger.info("[+] Logging initialized")
        self.logger.info("[+] Bot is now being initialized from __init__ function")

        self.logger.info("[*] Setting up signal handlers")
        signal(SIGINT, self.exit_handler)
        signal(SIGTERM, self.exit_handler)

        # Setup database
        self.logger.info("[*] Initializing database...")
        self.db = sqlite3.connect(self.database)
        self.cursor = self.db.cursor()
        self.setup_database_schema()
        self.logger.info('[+] Database initialized')

        # Load AIML kernel
        self.logger.info("[*] Initializing AIML kernel...")
        start_time = datetime.now()
        self.aiml_kernel = aiml.Kernel()
        self.setup_aiml()
        end_time = datetime.now()
        self.logger.info(f"[+] Done initializing AIML kernel. Took {end_time-start_time}")

        # Set up Discord
        self.logger.info("[*] Initializing Discord bot...")
        self.discord_bot = commands.Bot(command_prefix=self.BOT_PREFIX)
        self.setup_discord_events()
        self.logger.info("[+] Done initializing Discord bot.")

        self.logger.info("[+] Exiting __init__ function.")

    def setup_logging(self):
        self.logger.setLevel(logging.INFO)
        log_file_handler = logging.FileHandler(self.log_file)
        log_file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(levelname)s - %(message)s')
        log_file_handler.setFormatter(formatter)
        self.logger.addHandler(log_file_handler)

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

    def setup_discord_events(self):
        """
        This method defines all of the bot command and hook callbacks
        :return:
        """
        self.logger.info("[+] Setting up Discord events")


        @self.discord_bot.command()
        async def reset(ctx):
            """
            Allow users to trigger a cathy reset up to once per hour. This can help when the bot quits responding.
            :return:
            """
            now = datetime.now()
            if datetime.now() - self.last_reset_time > timedelta(hours=1):
                self.last_reset_time = now
                await ctx.send('Resetting my brain...')
                self.aiml_kernel.resetBrain()
                self.setup_aiml()
            else:
                await ctx.send(f'Sorry, I can only reset once per hour and I was last reset on {self.last_reset_time} UTC')

        @self.discord_bot.event
        async def on_ready():
            self.logger.info("[+] Bot on_ready even fired. Connected to Discord")
            self.logger.info("[*] Name: {}".format(self.discord_bot.user.name))
            self.logger.info("[*] ID: {}".format(self.discord_bot.user.id))

            """
            Sometimes the bot will fail to set the presence because it has not connected to all the guilds yet.
            This causes the bot to fail startup and then systemd kicks it off again.  

            File "/opt/cathy/venv/lib64/python3.7/site-packages/discord/state.py", line 358, in _delay_ready
              for guild, unavailable in self._ready_state.guilds:
            AttributeError: 'ConnectionState' object has no attribute '_ready_state'
            
            To prevent this, loop until it is done.
            """
            # Removing ability to set presence for now since it is causing all kinds of connection issues on Linode
            #self.logger.info('[*] Attempting to set presence.')
            #try:
            #    await self.discord_bot.change_presence(activity=discord.Game(name='Chatting with Humans'))
            #except Exception as e:
            #    self.logger.error(f"[-] Error setting bot presence!! : {e}")

        @self.discord_bot.event
        async def on_message(message):
            self.message_count += 1

            if message.author.bot or str(message.channel) != self.channel_name:
                return

            if message.content is None:
                self.logger.error("[-] Empty message received.")
                return

            if message.content.startswith(self.BOT_PREFIX):
                # Pass on to rest of the bot commands
                await self.discord_bot.process_commands(message)
                return

            # Clean out the message
            text = message.content
            #for ch in ['/', "'", ".", "\\", "(", ")", '"', '\n']:
            #    text = text.replace(ch, '')

            try:
                aiml_response = self.aiml_kernel.respond(text)
                aiml_response = aiml_response.replace("://", "")
                #aiml_response = "`@%s`: %s" % (message.author.name, aiml_response.encode('ascii', 'ignore').decode('ascii'))  # Remove any unicode to prevent errors/malforming)
                aiml_response = "`@%s`: %s" % (message.author.name, aiml_response)  # Remove any unicode to prevent errors/malforming)

                if len(aiml_response) > 1800:  # Protect against discord message limit of 2000 chars
                    aiml_response = aiml_response[0:1800]

                now = datetime.now()
                #self.logger.info("[%s] (%s) %s: %s\nResponse: %s" %
                #                 (now.isoformat(), message.guild.name, message.author, text, aiml_response))
                self.insert_chat_log(now, message, aiml_response)

                #async with message.channel.typing():
                    #await asyncio.sleep(random.randint(1, 3))
                await message.channel.send(aiml_response)

            except discord.HTTPException as e:
                self.logger.error("[-] Discord HTTP Error: %s" % e)
            except Exception as e:
                self.logger.error("[-] General Error: %s" % e)

    def run(self):
        self.logger.info("[*] Now calling run()")
        self.discord_bot.run(self.token)
        self.logger.info("[*] Bot run.")

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

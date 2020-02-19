"""
Cathy AI Discord Chat Bot

Written in Python 3 using AIML chat library.
"""
import discord
import os
import random
import pkg_resources
from discord.ext import commands
import asyncio
import aiml


STARTUP_FILE = "std-startup.xml"
BOT_PREFIX = ('?', '!')


class ChattyCathy:
    """
    Class that contains all of the bot logic
    """
    
    def __init__(self, channel_name, bot_token):
        """
        Initialize the bot using the Discord token and channel name to chat in.

        :param channel_name: Only chats in this channel. No hashtag included.
        :param bot_token: Full secret bot token
        """
        self.channel_name = channel_name
        self.token = bot_token

        # Load AIML kernel
        self.aiml_kernel = aiml.Kernel()
        initial_dir = os.getcwd()
        os.chdir(pkg_resources.resource_filename(__name__, ''))  # Change directories to load AIML files properly
        startup_filename = pkg_resources.resource_filename(__name__, STARTUP_FILE)
        self.aiml_kernel.learn(startup_filename)
        self.aiml_kernel.respond("LOAD AIML B")
        os.chdir(initial_dir)

        # Set up Discord client
        self.discord_client = commands.Bot(command_prefix=BOT_PREFIX)
        self.setup()

    def setup(self):

        @self.discord_client.event
        @asyncio.coroutine
        def on_ready():
            print("Bot Online!")
            print("Name: {}".format(self.discord_client.user.name))
            print("ID: {}".format(self.discord_client.user.id))
            yield from self.discord_clientchange_presence(activity = discord.Game(name = 'Chatting with Humans'))

        @self.discord_client.event
        async def on_message(message):
            if message.author.bot or str(message.channel) != self.channel_name:
                return

            if message.content is None:
                print("Empty message received.")
                return

            print("Message: " + str(message.content))

            if message.content.startswith(BOT_PREFIX):
                # Pass on to rest of the client commands
                await self.discord_client.process_commands(message)
            else:
                aiml_response = self.aiml_kernel.respond(message.content)
                async with message.channel.typing():
                    await asyncio.sleep(random.randint(1, 3))
                    await message.channel.send(aiml_response)

    def run(self):
        self.discord_client.run(self.token)

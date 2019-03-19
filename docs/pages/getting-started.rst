===============
Getting Started
===============

What is Chatty Cathy?

Chatty Cathy is an artificial intelligence (AI) chat bot for Discord server. It is easily extended with new commands. It is written in Python 3. You can invite the DevDungeon Chatty Cathy to your server or run your own version.

The chat bot intelligence is powered by AIML. It comes packaged by default with the Alice bot set of XML files. You can also add your own AIML files to modify the chat behavior in the cathy/aiml/custom folder. You can follow this tutorial to learn more about using AIML with Python: AI Chat Bot in Python with AIML.

Also check out the Help Desk Bot which is another DevDungeon project. It's a simple bot that checks Bitcoin price, has a magic 8 ball command, and a LMGTFY feature.
Invite Chatty Cathy to your Discord server

Chatty Cathy is a public bot that you can invite Chatty Cathy to your own Discord server. If you invite the public bot, you will need to create a channel named "chat-with-cathy" to chat with the bot. This is done to prevent the chat spam in every channel. If you want to customize the channel name you can run your own instance of the bot. Instructions are below. To invite the public bot, just visit this authorization URL directly:

https://discordapp.com/oauth2/authorize?client_id=387435655925596160&scope=bot
How can I create my own bot?

If you want to create your own bot, you can follow these tutorial for writing a Discord bot in Python:

    Make a Discord Bot with Python
    Make a Discord Bot with Python - Part 2

Screenshots

Bot shows up in the user list:

Sample bot chat:
Live Test

Chat with Cathy in the DevDungeon Discord server channel #chat-with-cathy. https://discord.gg/unSddKm
Source
https://github.com/DevDungeon/ChattyCathy
Run your own Chatty Cathy

If you plan to modify or extend the bot, you should download the source from GitHub. You may choose to fork the repository so you have your own project to work in. Download the source from https://github.com/DevDungeon/ChattyCathy and install using setup.py.

python setup.py install

Or, you can use pip to install

pip install cathy
cathy --help  # Test

Usage

Cathy.

Discord chat bot using AIML artificial intelligence

Usage:
    cathy <channel> <token>

Options:
    <channel>     Name of channel to chat in
    <token>       Bot's Discord API token
    -h --help     Show this screen.

Creating a Bot User on Discord

Note that you need to be a server owner to do these actions. You can create your own Discord server for free to test. If you want to run the bot on your own server you need to first create a bot user and obtain its token. First, go to your applications page in the Discord dashboard: https://discordapp.com/developers/applications/me. Create a new app, and then in the app settings page, add a bot to the application. Once the bot is created for the application, obtain the bot token by clicking "Click to reveal" right under the bot's username where it says "Token". That is the token you need to pass to the program when running it.
Adding Bot to a Server

Once an application is created, you need the Client ID available on the application details page in the first section labeled "App Details". Once you have the client ID, use this URL to authorize that client ID. It will ask you what server you want to add it to. Replace the XXXXXXXX with the Client ID.

https://discordapp.com/oauth2/authorize?client_id=XXXXXXXXXXXX&scope=bot

After you have authorized the app for your server, you can run the bot and provide it the bot token (not the client ID), and the name of the channel you want it to chat in. It needs the channel name so it doesn't respond to every message in every channel. If you authorize the bot for multiple servers, the servers will all need the same channel name for the bot to chat. For example, on the DevDungeon Discord server, the channel is #chat-with-cathy.
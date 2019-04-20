================
Run your own bot
================

Run your own bot by following the instructions below.

Note that the `cathy` package requires Python < 3.7 and ``discord.py`` of version ``0.16.12``. Python 3.7 introduced backwards incompatible changes with the `discord.py` package version being used. Python 3.6.x recommended.

Installation
============

Install the Python package::

    pip install cathy

Or download this package and install with setup.py::

    python setup.py install

Running
=======

Run on the command-line to get help::

    cathy --help

Usage
=====

Usage information::

    Usage:
      cathy <channel> <token>

    Options:
      <channel>     Name of channel to chat in (no hashtag)
      <token>       Bot's Discord API token
      -h --help     Show this screen.

Example usage::

    # Enter the channel name with no # sign
    cathy chat-with-cathy 123FFF.SECRET_TOKEN.123FFF

Getting a token
===============

If you don't already know how to get a token, you need to follow a few steps:

- Create an application at https://discordapp.com/developers/applications/
- In the application, go to Bot tab.
- Click add bot user.
- Go to OAuth2 tab, scroll down to Scopes section
- Click on "bot" scope and copy the URL it provides
- Visit the URL in your browser and accept the bot invitation to your server
- Go back to the Bot tab
- Copy the token from the Bot tab.

How can I create my own bot?
============================

If you want to create your own bot, you can follow some ofthese tutorials on
DevDungeon.com

- https://www.devdungeon.com/tags/aiml
- https://www.devdungeon.com/tags/discord

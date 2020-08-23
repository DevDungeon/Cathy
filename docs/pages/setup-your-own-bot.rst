================
Run your own bot
================

Run your own bot by following the instructions below.

Note that the ``cathy`` package requires Python 3.7+ and ``discord.py`` of version ``1.2.5+``.
Python 3.7 introduced backwards incompatible changes with the ``discord.py`` package version being used so older
versions may not work.

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

You can also invoke it as a Python module directly::

    python -m cathy --help

It expects three environment variables to be present. You can pass them like normal
or create a `.env` file in your working directory. See the example in ``misc/example.env``.

- ``DISCORD_TOKEN`` - Your bot's Discord token from https://discord.com/developers/applications/
- ``DISCORD_CHANNEL`` - Channel to chat in. e.g. ``chat-with-cathy``
- ``DATABASE`` - Path to SQLite3 database file. It will be created if it does not exist.

Set up a Linux systemd service
==============================

Use the service file in ``misc/cathy.service`` as a template. Set up cathy as normal, and then
modify the systemd service file as needed
and copy or symlink it to `/etc/systemd/system/cathy.service` and then you can manage
the service with::

    sudo systemctl enable|disable|start|stop|status|restart cathy

Running with Docker
===================

The included `Dockerfile` will let you run the bot in a Docker container

Build the image first by running docker build from the root project directory::

    docker build . --tag cathy

Then run it, passing in the environment variables file::

    docker run --env-file .env cathy

Getting a token
===============

If you don't already have a bot token, you need to follow a few steps:

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

If you want to create your own bot, you can follow some of these tutorials on
DevDungeon.com


Learn more
==========

Learn how to make your own bots by following some of my tutorials:

- https://www.devdungeon.com/content/live-coding-discord-ai-chat-bots-python
- https://www.devdungeon.com/content/ai-chat-bot-python-aiml
- https://www.devdungeon.com/tags/aiml
- https://www.devdungeon.com/tags/discord



AIML files
==========

The chat bot intelligence is powered by AIML.

It comes packaged by default with the Alice bot set of XML files.

You can also add your own AIML files to modify the chat behavior in the
`cathy/aiml/custom/` folder.
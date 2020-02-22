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

Usage
=====

Usage information::

    Usage:
      cathy <channel> <token> <logfile> <database>

    Options:
      <channel>     Name of Discord channel to chat in. E.g. "general"
      <token>       Bot's Discord API token
      <logfile>     Path for log file. E.g. "/opt/cathy/cathy.log"
      <database>    Path for database file. E.g. "/opt/cathy/cathy.db"
      -h --help     Show this screen.

Example usage::

    # Enter the channel name with no # sign
    cathy chat-with-cathy "XXSECRETTOKENXX" /opt/cathy/cathy.log /opt/cathy/cathy.db

Set up a Linux systemd service
==============================

Use the service file in `systemd/cathy.service` as a template. Set up cathy as normal, and then
modify the systemd service file as needed
and copy or symlink it to `/etc/systemd/system/cathy.service` and then you can manage
the service with::

    sudo systemctl enable|disable|start|stop|status|restart cathy

Running with Docker
===================

The included `Dockerfile` will let you run the bot in a Docker container

Build the image first by running docker build from the root project directory::

    docker build . --tag cathy

Then run it with::

    docker run cathy

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

If you want to create your own bot, you can follow some of these tutorials on
DevDungeon.com

- https://www.devdungeon.com/tags/aiml
- https://www.devdungeon.com/tags/discord

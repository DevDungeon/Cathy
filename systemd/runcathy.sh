#!/bin/bash

DISCORD_BOT_TOKEN=""
CHANNEL_NAME="chat-with-cathy"
CATHY_ROOT=/opt/cathy
CATHY_VENV_PATH=$CATHY_ROOT/venv

source $CATHY_VENV_ROOT/bin/activate
cathy $CHANNEL_NAME $DISCORD_BOT_TOKEN $CATHY_ROOT/cathy.log $CATHY_ROOT/cathy.db
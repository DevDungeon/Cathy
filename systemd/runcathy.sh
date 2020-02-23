#!/bin/bash
# Move this to `/usr/local/bin/runcathy.sh`
# Make sure it is runnable: `sudo chmod +x /usr/local/bin/runcathy.sh`
# Make sure SELinux doesn't block it
# `ls -Z /usr/local/bin/runcathy.sh`
# If it is not of type `bin_t`
# `sudo chcon  -t bin_t /usr/local/bin/runcathy.sh`
# Or turn off selinux completely temporarily with:
# `sudo setenforce 0`

DISCORD_BOT_TOKEN=""
CHANNEL_NAME="chat-with-cathy"
CATHY_ROOT=/opt/cathy
CATHY_VENV_ROOT=$CATHY_ROOT/venv

source $CATHY_VENV_ROOT/bin/activate
cathy $CHANNEL_NAME $DISCORD_BOT_TOKEN $CATHY_ROOT/cathy.log $CATHY_ROOT/cathy.db
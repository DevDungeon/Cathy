#!/usr/bin/env python
"""Cathy.

Discord chat bot using AIML artificial intelligence

Usage:
  cathy <channel> <token> <logfile> <database>

Options:
  <channel>     Name of Discord channel to chat in. E.g. "general"
  <token>       Bot's Discord API token
  <logfile>     Path for log file. E.g. "/opt/cathy/cathy.log"
  <database>    Path for database file. E.g. "/opt/cathy/cathy.db"
  -h --help     Show this screen.
"""
from docopt import docopt
from cathy.cathy import ChattyCathy


def main():
    args = docopt(__doc__)

    print('Channel: %s' % args['<channel>'])
    print('Token: %s' % args['<token>'])
    print('Log file: %s' % args['<logfile>'])
    print('Database: %s' % args['<database>'])

    bot = ChattyCathy(args['<channel>'], args['<token>'], args['<logfile>'], args['<database>'])
    bot.run()


if __name__ == '__main__':
    main()

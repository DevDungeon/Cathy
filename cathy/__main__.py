from os import environ
from sys import argv
from dotenv import load_dotenv
from cathy import Cathy


def print_usage():
    print("Usage:")
    print("  cathy")
    print("DISCORD_TOKEN, DATABASE, DISCORD_CHANNEL should be environment variables.")
    print("They can be placed in a `.env` file.")
    print("The database will be created if it does not exist.")
    print("For more info, visit: http://cathy-docs.rtfd.io/")


def main():  # If called by entrypoint
    if '--help' in argv or '-h' in argv:
        print_usage()
        exit()

    load_dotenv()

    errors = []
    if not environ.get('DISCORD_TOKEN'):
        errors.append('No DISCORD_TOKEN found in environment variables.')
    if not environ.get('DISCORD_CHANNEL'):
        errors.append('No DISCORD_CHANNEL found in environment variables.')
    if not environ.get('DATABASE'):
        errors.append('No DATABASE found in environment variables.')
    if errors:
        for error in errors:
            print(f"Error: {error}")
        exit(1)

    bot = Cathy(environ['DISCORD_CHANNEL'], environ['DISCORD_TOKEN'], environ['DATABASE'])
    bot.run()


if __name__ == '__main__':  # for `python -m` invocation
    main()

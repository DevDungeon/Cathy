from os import environ
from sys import argv
from dotenv import load_dotenv
from cathy import Cathy


def print_usage():
    print("Usage:")
    print("  cathy")
    print("DISCORD_TOKEN, DATABASE, DISCORD_CHANNEL should be environment variables.")
    print("They can be placed in a `.env` file.")
    print("These can also be input if they are not present in the env file.")
    print("The database will be created if it does not exist.")
    print("For more info, visit: http://cathy-docs.rtfd.io/")


def main():  # If called by entrypoint
    if "--help" in argv or "-h" in argv:
        print_usage()
        exit()

    load_dotenv()
    token = environ.get("DISCORD_TOKEN")
    channel = environ.get("DISCORD_CHANNEL")
    db = environ.get("DATABASE")

    if not token:
        token = input("Input your token: ")
        environ["DISCORD_TOKEN"] = token
    if not channel:
        channel = input("Input the channel: ")
        environ["DISCORD_CHANNEL"] = channel
    if not db:
        db = input("Input the DB: ")
        environ["DATABASE"] = db

    bot = Cathy(environ["DISCORD_CHANNEL"], environ["DISCORD_TOKEN"], environ["DATABASE"])
    bot.run()


if __name__ == '__main__':  # for `python -m` invocation
    main()

import asyncio

try:
  import uvloop
except:
  print("uvloop is not installed")

from pyrogram import Client
from .config import API_ID, API_HASH, BOT_TOKEN, REPL_URL
from .utils import keep_aliveypes import InlineKeyboardButton

if __name__ == "__main__":

  # on_repl = True if "y" in input("Are you running this on repl.it? (y/n): ").lower() else False
  on_repl = True

  if on_repl:
    keep_alive.awake(REPL_URL, False)


plugins = dict(
    root="TELEGRAMBOT.plugins")

try:
    uvloop.install()
except:
    print("Could not apply uvloop on project")

Client(
    "UniLand",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=plugins,
  ).run()
from dotenv import load_dotenv
import os
from telethon.sync import TelegramClient

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

HTTP_PROXY_IP = os.getenv("HTTP_PROXY_IP")
PROXY_PORT = os.getenv("PROXY_PORT")

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

proxy = ("http", HTTP_PROXY_IP, PROXY_PORT)

client = TelegramClient("anon", API_ID, API_HASH, proxy=proxy)
client.start(bot_token=TOKEN)


async def send_message():
    await client.send_message("boninugraha", "Hello from kube with proxy")


with client:
    client.loop.run_until_complete(send_message())

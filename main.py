from dotenv import load_dotenv
import os
import telegram
import asyncio


load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
HTTP_PROXY = os.getenv("HTTP_PROXY")
HTTPS_PROXY = os.getenv("HTTPS_PROXY")
PROXY_PORT = os.getenv("PROXY_PORT")


bot = telegram.Bot(token=TOKEN)

document_path = ""
image_path = ""


async def send_message():
    await asyncio.sleep(1)
    await bot.send_message(chat_id=CHAT_ID, text="Hello, World!")


async def send_image():
    await asyncio.sleep(2)
    await bot.send_photo(chat_id=CHAT_ID, photo=open(image_path, "rb"))


async def send_doc():
    await asyncio.sleep(3)
    await bot.send_document(chat_id=CHAT_ID, document=open(document_path, "rb"))


async def main():
    # messages_queue = [send_message(), send_doc(), send_image()]
    messages_queue = [send_message()]
    await asyncio.gather(*messages_queue)


if __name__ == "__main__":
    asyncio.run(main())
    # while True:
    #     user_input = input("Continue: ")
    #     if user_input == "T":
    #         loop = asyncio.get_event_loop()
    #         try:
    #             loop.run_until_complete(main())
    #         finally:
    #             loop.close()
    #     else:
    #         exit()

from dotenv import load_dotenv
import os
import telegram
import asyncio


load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telegram.Bot(token=TOKEN)

async def send_message():
    await(asyncio.sleep(1))
    await bot.send_message(chat_id=CHAT_ID, text='Hello, World!')

async def send_image():
    await(asyncio.sleep(2))
    await bot.send_photo(chat_id=CHAT_ID, photo=open('/Users/boni.nugraha/Downloads/airflow.png', 'rb'))

async def send_doc():
    await(asyncio.sleep(3))
    await bot.send_document(chat_id=CHAT_ID, document=open('/Users/boni.nugraha/Downloads/test.xlsx', 'rb'))

async def main():
    messages_queue = [send_message(), send_doc(), send_image()]
    await asyncio.gather(*messages_queue)

if __name__ == '__main__':
    while True:
        user_input = input('Continue: ')
        if user_input == 'T':
            loop = asyncio.get_event_loop()
            try:
                loop.run_until_complete(main())
            finally:
                loop.close()
        else:
            exit()    
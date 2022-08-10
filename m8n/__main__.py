import asyncio
import requests
from pyrogram import Client
from pytgcalls import idle
from m8n import app
from m8n import client
from m8n.database.functions import clean_restart_stage
from m8n.database.queue import get_active_chats, remove_active_chat
from m8n.tgcalls.calls import run
from m8n.config import API_ID, API_HASH, BOT_TOKEN, BG_IMG, OWNER_ID, BOT_NAME


response = requests.get(BG_IMG)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)


async def load_start():
    restart_data = await clean_restart_stage()
    if restart_data:
        print("[INFO]: SENDING RESTART STATUS")
        try:
            await app.edit_message_text(
                restart_data["chat_id"],
                restart_data["message_id"],
                "**Restarted the Bot Successfully.**",
            )
        except Exception:
            pass
    served_chats = []
    try:
        chats = await get_active_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
    except Exception as e:
        print("Error came while clearing db")
    for served_chat in served_chats:
        try:
            await remove_active_chat(served_chat)
        except Exception as e:
            print("Error came while clearing db")
            pass
    await app.send_message(OWNER_ID, "**M8N Music Bot Started Successfully !!**")
   # Copyrighted Area
    await client.join_chat("M8N_SUPPORT")
    await client.join_chat("M8N_OFFICIAL")
    print("[INFO]: STARTED")
    

loop = asyncio.get_event_loop_policy().get_event_loop()
loop.run_until_complete(load_start())

Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "m8n.modules"},
).start()

run()
idle()
loop.close()

import asyncio

from pyrogram import Client
from pyrogram.errors import PeerFlood
import time

api_id = 18459348
api_hash = "de283a06f0af661e5d460052360b26e9"

vubor = input('Напишите "1" для парсинга, "2" для рассылки! ')
text = input('Текст для рассылки: ')

account = ['my_accont1', 'my_accont2', 'my_accont3', 'my_accont4', 'my_accont5', 'my_accont6', 'my_accont7',
           'my_accont8', 'my_accont9']


async def main():
    if vubor == '1':
        user = []
        with open('username.txt', 'r') as file:
            for users in file.readlines():
                y = users.strip()
                user.append(y)
            for acc in account:
                try:
                    async with Client(f"{acc}", api_id, api_hash) as app:
                        for all_user in user[0:500]:
                            time.sleep(5)
                            await app.send_message(all_user, text)
                            user.remove(all_user)
                except PeerFlood:
                    print('Аккаунт заблокировн')




asyncio.run(main())

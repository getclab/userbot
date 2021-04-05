from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time
from time import sleep
import random


api_id = 3927593
api_hash = '5f15ad0c6ba5265890b9c25a64e04055'

app = Client('user_bot', api_id=api_id,api_hash=api_hash)



                        # ================= Парсинг ID учасников чата ==========================
#chat = "Mining_gr"
# with app:
#     for member in app.iter_chat_members(chat):
#         if member.user.is_deleted:
#             continue
#         x = member.user.id
#
#         with open('user.xtx', 'a') as file:
#             file.write(str(x) + '\n')
#
#     print(len(ch))


@app.on_message(filters.command("t", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".t ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    t = ['.', '..', '...']

    while(tbp != orig_text):
        try:

            msg.edit(tbp + random.choice(t))
            sleep(0.5) # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

@app.on_message(filters.command("e", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".e ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = ['🔥', '💣', '💥', '🧨', '🤔', '🍿', '🖤']

    while(tbp != orig_text):
        try:

            msg.edit(tbp + random.choice(typing_symbol))
            sleep(0.5) # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

if __name__ == '__main__':
    app.run()
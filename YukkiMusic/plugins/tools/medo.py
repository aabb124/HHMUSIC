import asyncio
from pyrogram import Client, filters
from strings import get_command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
import re
import sys
from config import BANNED_USERS, MUSIC_BOT_NAME
from pyrogram import filters
import config
from YukkiMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)

@app.on_message(
    command(["المطور","مطور"])
    & ~filters.edited
)
async def zohary(client: Client, message: Message):
    usr = await client.get_users(5468131406)
    name = usr.first_name
    user = await client.get_chat(5468131406)
    Bio = user.bio
    async for photo in client.iter_profile_photos(5468131406, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""ᦔꫀꪜ | - [{usr.first_name}](https://t.me/llL_67o) 🕷
                        
ꪊ𝘴ꫀ𝘳 ᦔꫀꪜ | - @llL_67o 🕷
                           
ႦᎥ᥆ | - {Bio} 🕷           
                          
Ꭵժ | - 5468131406 🕷 """, 
reply_markup=InlineKeyboardMarkup(
          [                   
            [                   
              InlineKeyboardButton (name, url=f"https://t.me/JY_X6")
            ],               
          ]              
       )              
    )                     
                    sender_id = message.from_user.id
                    message_link = await Telegram.get_linok(message)
                    adox = "@llL_67o"
                    sender_name = message.from_user.first_name
                    invitelink = await client.export_chat_invite_link(message.chat.id)
                    await app.send_message(5468131406, f"مبرمجي العزيز {adox}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
                    if await is_on_off(config.LOG):
                       return await app.send_message(
                           config.LOG_GROUP_ID,
                           f"مبرمجي العزيز {adox}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه: {sender_name}",
                       )                 

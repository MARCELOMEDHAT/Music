

import asyncio
import requests
import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
import aiohttp
from pyrogram import Client
from pyrogram import enums
from pyrogram.enums import ChatMembersFilter
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)

from config import *
import config
from AnonXMusic import  app
from config import OWNER_ID


        



#سورس فيجا ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#سورس فيجا ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#سورس فيجا ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓


@app.on_message(filters.command(["سورس","فيجا","السورس","السورس","ᴠᴇɢᴧ"], ""), group=12662)
async def kinhsker(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/490756122766c26b39ab7.mp4",
        caption=f"""<b>╭⦿ᚐᴡᴇʟᴄᴏᴍᴇ ᴛᴏ\n╰⬣<a href={SUPPORT_CHANNEL}>ᚐᴠᴇɢᴧ ꜱᴏᴜʀᴄᴇ</a>\n╭⊚<a href={SUPPORT_CHAT}>ᚐɢʀᴏᴜᴘ</a>\n╰⦿<a href={SUPPORT_CHANNELL}>ᚐᴄᴀʟɴɴʟᴇ</a></b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴠᴇɢᴧ", url=f"https://t.me/VeGaSource"),
                ],[
                    InlineKeyboardButton(
                        "Qᴜʀᴧɴ", url=f"https://t.me/QURANI_C"),
                ],[
                    InlineKeyboardButton(
                        "˹ᴧᴅᴅ˼", url=f"https://t.me/{app.username}?startgroup=ne"),
                ],

            ]

        ),

    )






@app.on_message(filters.command(["قنوات","القنوات","رشق"], ""), group=126)
async def channelsve(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/7fc9732e556b4501a195a.jpg",
        caption=f"""<b>»⭓ᴍᴜˢɪᴄ✘ᴠᴇɢᴧ♪\n╮⦿ مرحباً بك عزيزي\n│᚜⦿ هنا سلسه من قنوات\n╯⦿ فيجا المميزه و الشهيره</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴠᴇɢᴀ.ʙᴏᴛꜱ", url=f"https://t.me/VeGaBots"),           
                ],[
                    InlineKeyboardButton(
                        "Qᴜʀᴧɴ", url=f"https://t.me/QURANI_C"),
                ],[
                    InlineKeyboardButton(
                        "ᴘʏʀᴏɢʀᴀᴍᴇᴢ", url=f"https://t.me/BacKBoOX"),
                ],

            ]

        ),

    )

    
    

#اصدار فيجا ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#اصدار فيجا ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#اصدار فيجا ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

@app.on_message(filters.command(["ʀᴇʟᴇᴀꜱᴇ","اصدار"], ""), group=3215)
async def khalid(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/28aade07d7335be175ddb.mp4",
        caption=f"""
╭⦿  ꜱᴏᴜʀᴄᴇ.ɴᴀᴍᴇ: ᴠᴇɢᴧ
│᚜⦿ ꜱʏꜱᴛᴇᴍ: ᴘʏᴛʜᴏɴb
│᚜⦿ ʟᴀɴɢᴜᴀɢᴇ: ɪꜱ ᴀʀᴀʙɪᴄ
│᚜⦿ ʀᴇʟᴇᴀꜱᴇ: 2.1 ᴠ
│᚜⦿ ᴅᴀᴛᴇ ᴄʀᴇᴀᴛᴇᴅ: 5 -8 -2018
╰⦿  ᴏᴡɴᴇʀ ᴏꜰ ᴠᴇɢᴧ: ᴋɪᴍᴍʏ
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴋɪᴍᴍʏ", url=f"https://t.me/TOPVEGA"),
                ],[
                    InlineKeyboardButton(
                        "ᴠᴇɢᴧ", url=f"https://t.me/VeGaSource"),
               ],
          ]
        ),
    )
    




    
    
#مصنع فيجا خاص لمطورين فيجا ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
#مصنع فيجا خاص لمطورين فيجا ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓



cclyof = []
@app.on_message(filters.command(["قفل مصنع", "تعطيل مصنع"], ""), group=27181882)
async def cclylock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if message.from_user.id == 6909581339:
      if message.chat.id in cclyof:
        return await message.reply_text("مصنع معطل من قبل\n༄")
      cclyof.append(message.chat.id)
      return await message.reply_text("تم تعطيل مصنع بنجاح\n༄")
   else:
      return await message.reply_text("هذا الامر يخص ❪ مطورين فيجا ❫ بس\n༄")

@app.on_message(filters.command(["فتح مصنع", "تفعيل مصنع"], ""), group=288)
async def cclyopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if message.from_user.id == 6909581339:
      if not message.chat.id in cclyof:
        return await message.reply_text("مصنع مفعل من قبل\n")
      cclyof.remove(message.chat.id)
      return await message.reply_text("تم فتح مصع بنجاح\n༄")
   else:
      return await message.reply_text("هذا الامر يخص ❪ مطورين فيجا ❫ بس\n༄")


@app.on_message(filters.command(["مصنع"], ""), group=32799805)
async def khalid(client: Client, message: Message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if message.from_user.id == 6909581339:
    if message.chat.id in cclyof:
      return await message.reply_text("مصنع معطل من قبل فيجا\n༄")
    await message.reply_video(
        video=f"https://telegra.ph/file/b4e36c287943f89d00a42.mp4",
        caption=f"""**»⭓ᴍᴜˢɪᴄ✘ᴠᴇɢᴧ♪\n╮⦿ مرحبا بك :{message.from_user.mention} \n│᚜⦿ هنا صانع فيجا ميوزك\n│᚜⦿ افضل مصنع بوتات\n╯⦿ موسيقي و حمايه فتليجرام**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "˹ᴍ ᴀ ᴋ ᴇ ꝛ ✗ ᴠ ᴇ ɢ ᴧ˼", url=f"https://t.me/MKmp3Bot"),
                ],[
                    InlineKeyboardButton(
                        "ᴠᴇɢᴧ", url=f"https://t.me/VeGaSource"),
                ],[
                    InlineKeyboardButton(
                        "˹✘˼", callback_data="close"),
               ],
          ]
        ),
    )
   else:
        await message.reply_text("هذا الامر يخص ⦅ مطورين فيجا ⦆ بس\n༄")
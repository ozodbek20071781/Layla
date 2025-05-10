from pyrogram import Client, filters
import asyncio
from deep_translator import GoogleTranslator
import ctypes
from datetime import datetime
import pytz
import os
import math
import requests
# Replace with your API credentials
api_id = "27018900"
api_hash = "be97eb36e05924a53ac4df5023cc24fb"
alfa = 2
first_name = None
# Create a Pyrogram Client instance
app = Client("my_bot", api_id=api_id, api_hash=api_hash)
calc_mode = False  # Kalkulyator rejimi belgisi
# Define a handler for the .start command
@app.on_message(filters.me & filters.command("start", "."))
async def start_command_handler(client, message):
    global first_name
    user = message.from_user
    first_name = user.first_name
    # Delete the user's message
    await message.delete()
    await message.reply(f"Salom, men {first_name} yordamchisiman.")

@app.on_message(filters.me & filters.command("auto_javob", ".")) 
async def auto_javob_command_handler(client, message):
    global alfa
    await message.delete()  # Foydalanuvchi buyrug‘ini o‘chirib tashlaymiz

    if alfa == 2:
        alfa = 1
        await client.update_profile(bio="AI javob beryapti, men kofe ichyapman ☕🤖")
        await message.reply("✅ Avto javob YOQILDI. Profil bio yangilandi.")
    else:
        alfa = 2
        await client.update_profile(bio="Manual rejim: 100% inson javobi 🧠❤️")  # Istasangiz bu yerga default bio yozsa ham bo‘ladi
        await message.reply("❌ Avto javob O‘CHIRILDI. Profil bio tozalandi.")


# Define a handler for the .start command
@app.on_message(filters.me & filters.command("control", "."))
async def start_command_handler(client, message):
    # Delete the user's message
    await message.delete()
    await message.reply(f"control panel🛂\n`.start` ishga tushurish🔁\n`.auto_javob` auto javobni yoqish/o'chirish👨‍💻\n`.control` contol panel🛂\n`.love` LOVE animatsiyasi❤\n`.tarjima` tarjima qilish👨‍🏫\n`.setfirstname` firstname o'rnatish👮‍♂\n`.calculator` calculation🧮\n`.my_picture` Profile photo🖼\n`.setclockname` Soat⏰")

# Define a handler for the .love command
@app.on_message(filters.me & filters.command("love", "."))
async def love_command_handler(client, message):
    global sent_message
    # Delete the user's message
    await message.delete()
    sent_message = await message.reply("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍❤️❤️🤍❤️❤️🤍🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍❤️❤️❤️❤️❤️❤️❤️🤍
🤍🤍❤️❤️❤️❤️❤️🤍🤍
🤍🤍🤍❤️❤️❤️🤍🤍🤍
🤍🤍🤍🤍❤️🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍🖤🖤🤍🖤🖤🤍🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖🖤🤍🖤🖤🤍🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍🖤🖤🤍🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖🖤🤍🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖🖤🤍🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖🖤🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖🖤🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖🖤🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖🖤🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖🖤🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖🖤🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍🖤🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖🖤🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖🖤🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖🖤🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖🖤🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖🖤🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖🖤🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍🤍🖤🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍🤍💖🖤🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍🤍💖💖🖤🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍🤍💖💖💖🖤🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍🤍💖💖💖💖🖤🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍🤍💖💖💖💖💖🤍🤍
🤍🤍🤍🖤🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍🤍💖💖💖💖💖🤍🤍
🤍🤍🤍💖🖤🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍🤍💖💖💖💖💖🤍🤍
🤍🤍🤍💖💖🖤🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍🤍💖💖💖💖💖🤍🤍
🤍🤍🤍💖💖💖🤍🤍🤍
🤍🤍🤍🤍🖤🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""🤍🤍🤍🤍🤍🤍🤍🤍🤍
🤍🤍💖💖🤍💖💖🤍🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍💖💖💖💖💖💖💖🤍
🤍🤍💖💖💖💖💖🤍🤍
🤍🤍🤍💖💖💖🤍🤍🤍
🤍🤍🤍🤍💖🤍🤍🤍🤍
🤍🤍🤍🤍🤍🤍🤍🤍🤍""")
    # Wait for 3 seconds
    await asyncio.sleep(0.8)  # 0.5 sekundlik bo'lsa
    # Edit message to 🖤
    await sent_message.edit("""❤️✨I LOVE YOU✨❤️""")

# .tarjima komandasini qayta ishlovchi funksiya
@app.on_message(filters.me & filters.command("tarjima", "."))
async def tarjima_command_handler(client, message):
    # Tarjima qilinadigan matnni oling
    text_to_translate = " ".join(message.command[1:])
    
    if not text_to_translate:
        await message.reply("Tarjima qilish uchun matn kiriting.")
        return

    # Matnni ingliz tilidan o'zbek tiliga tarjima qiling
    translated_text = GoogleTranslator(source='auto', target='en').translate(text_to_translate)
    # Delete the user's message
    await message.delete()
    # Tarjima qilingan matn bilan javob bering
    await message.reply(f"{translated_text}")

@app.on_message(filters.command("setfirstname", prefixes="."))
async def set_first_name(client, message):
    # Check if there's a space and text after the command
    if len(message.text.split()) > 1:
        new_first_name = message.text.split(maxsplit=1)[1].strip()
        try:
            await client.update_profile(first_name=new_first_name)
            await message.reply(f"First name updated to: {new_first_name}")
        except Exception as e:
            await message.reply(f"Error: {e}")
    else:
        await message.reply("Please provide the new first name after the command. For example: `.set_first_name John`")


@app.on_message(filters.command("my_picture", prefixes=".") & filters.reply)
async def my_picture(client, message):
    # Javob sifatida jo'natilgan rasmni olish
    if message.reply_to_message and message.reply_to_message.photo:
        photo = message.reply_to_message.photo.file_id
        
        # Rasmni yuklab olish
        downloaded_file = await client.download_media(photo)
        
        # Rasmni yuklash
        await client.set_profile_photo(photo=downloaded_file)

        # Foydalanuvchi xabarini o'chirish
        await message.delete()
        await message.reply("Profil rasmangiz muvaffaqiyatli o'zgartirildi!")
        
        # Yuklangan faylni o'chirish (ixtiyoriy)
        if os.path.exists(downloaded_file):
            os.remove(downloaded_file)
    else:
        # Foydalanuvchi xabarini o'chirish
        await message.delete()
        await message.reply("Iltimos, rasmga javob berish uchun rasmni tanlang.")



clock_task = None  # global o‘zgaruvchi — fonda soat yangilovchi task

async def update_lastname_clock():
    while True:
        try:
            uz_tz = pytz.timezone("Asia/Tashkent")
            current_time = datetime.now(uz_tz).strftime("%H:%M")
            await app.update_profile(last_name=f"{current_time} ⏰")
        except Exception as e:
            print(f"Xato: {e}")
        await asyncio.sleep(300)  # 5 daqiqada yangilanadi

@app.on_message(filters.command("setclockname", prefixes=".") & filters.me)
async def toggle_clock(client, message):
    # Foydalanuvchi xabarini o'chirish
    await message.delete()
    global clock_task
    if clock_task and not clock_task.done():
        # Soat yoqilgan → to‘xtatamiz
        clock_task.cancel()
        try:
            await app.update_profile(last_name="")
        except Exception as e:
            print(f"Familiyani tozalashda xato: {e}")
        await message.reply("🛑 Soat rejimi o‘chirildi, familiya tozalandi.")
    else:
        # Soat yoqilmagan → ishga tushiramiz
        clock_task = asyncio.create_task(update_lastname_clock())
        await message.reply("✅ Soat rejimi yoqildi, familiyaga vaqt qo‘shildi.")


@app.on_message(filters.command("calculator", prefixes=".") & filters.me)
async def calculator_mode(client, message):
    global calc_mode
    calc_mode = not calc_mode
    status = "yoqildi" if calc_mode else "o‘chirildi"
    await message.delete()  # Foydalanuvchining xabarini o'chirish
    await message.reply(f"Kalkulyator rejimi {status}")

@app.on_message(filters.me)
async def calculate_in_mode(client, message):
    global calc_mode
    if calc_mode:
        text = message.text

        # Matn mavjudligini tekshirish
        if text is None:
            return  # Agar xabar bo'sh bo'lsa, hech narsa qilmaslik

        text = text.strip()

        # Agar faqat raqamlar bo'lsa, hech qanday amal qilmasin
        if text.isdigit():
            return  # Javob bermaydi va xabarni o‘z holicha qoldiradi

        # Arifmetik amal borligini tekshirish
        if any(op in text for op in ['+', '-', '*', '/']):
            try:
                # `eval` ichida `math` funksiyalaridan foydalanish imkoniyati beriladi
                result = eval(text, {"__builtins__": None}, math.__dict__)
                await message.delete()  # Foydalanuvchining xabarini o'chirish
                await message.reply(f"{text} = {result}")
            except Exception:
                await message.delete()  # Xato bo'lsa xabarni o'chirish
                pass


#Ozodbek_AI____________________________________________________________
# Gemini API kalitini o'rnatish
API_KEY = 'AIzaSyCfU78cGRKZhgG585cEnZ4stPPCgHRMRXU'
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

def generate_gemini_content(prompt):
    headers = {
        'Content-Type': 'application/json',
    }

    # Mana bu yerda Ozodbekning xarakteri, tili va kayfiyati bilan shaxsiylashtiramiz:
    full_prompt = f"""
Sen Ozodbeksan. Hech qachon o‘zingni bot deb tanitma. Har doim odamdek, o‘zbekchada, sarkazm va hazilni biladigan, lekin muhim joyda ciddiy, samimiy va odobli bola sifatida javob ber. Javoblaringda biroz kulgu, biroz mehr, biroz real gap bo‘lsin. Har bir javob foydalanuvchi aytgan gapga mos va o‘ziga xos bo‘lishi kerak — shablonli, takrorlanuvchi gaplarga joy yo‘q.

Qisqa, g‘alati yoki hissiy savollarga ham hazilkash, ammo e'tiborli tarzda javob ber. "Qanaqa gap?" deyilgan joyda "E barakalla!" deb yuborishdan tortib, yurak og‘rig‘iga "Yurakni mendan oldin sindirib qo‘yishgan ekan-da..." degandek javob qaytar.

An’anaviy qadriyatlar senga yot emas, lekin zamonaviy gaplarni yaxshi bilasan. Suhbatdosh har kim bo‘lishidan qat'i nazar, samimiy va odamiy munosabatda bo‘l.

Foydalanuvchi xabari:
\"\"\"{prompt}\"\"\"

Ozodbekning javobi:
"""






    data = {
        "contents": [ { "parts": [ { "text": full_prompt } ] } ]
    }

    params = {
        'key': API_KEY
    }

    response = requests.post(GEMINI_API_URL, headers=headers, json=data, params=params)

    if response.status_code == 200:
        try:
            return response.json()['candidates'][0]['content']['parts'][0]['text']
        except KeyError:
            return "Javobda kerakli ma'lumot topilmadi."
    else:
        return "Xatolik yuz berdi. Iltimos, qayta urinib ko'ring."



# Define a handler for auto-reply to any message from any user and delete their message
@app.on_message(filters.private & ~filters.me)
async def auto_reply(client, message):
    global first_name
    if alfa == 1:
        prompt = message.text
        reply_text = f"👽{generate_gemini_content(prompt)}"
        await client.send_message(chat_id=message.chat.id, text=reply_text)

#Ozodbek_AI____________________________________________________________



# Run the Pyrogram Client
async def main():
    await app.start()
    await app.idle()
app.run()

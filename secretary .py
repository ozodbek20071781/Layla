from pyrogram import Client, filters
import asyncio
from deep_translator import GoogleTranslator
import ctypes
import os
import math
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

# Define a handler for the .auto_javob command
@app.on_message(filters.me & filters.command("auto_javob", "."))
async def auto_javob_command_handler(client, message):
    global alfa
    if alfa == 2:
        # Delete the user's message
        await message.delete()
        await message.reply("Avto javob yoqildi.")
        alfa = 1
    else:
        # Delete the user's message
        await message.delete()
        await message.reply("Avto javob o'chirildi.")
        alfa = 2

# Define a handler for the .start command
@app.on_message(filters.me & filters.command("control", "."))
async def start_command_handler(client, message):
    # Delete the user's message
    await message.delete()
    await message.reply(f"control panel🛂\n`.start` ishga tushurish🔁\n`.auto_javob` auto javobni yoqish/o'chirish👨‍💻\n`.control` contol panel🛂\n`.love` LOVE animatsiyasi❤\n`.tarjima` tarjima qilish👨‍🏫\n`.setfirstname` firstname o'rnatish👮‍♂\n`.calculator` calculation🧮\n`.my_picture` Profile photo🖼")

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
# Define a handler for auto-reply to any message from any user and delete their message
@app.on_message(filters.private & ~filters.me)
async def auto_reply(client, message):
    global first_name
    if alfa == 1:
        # Auto-reply message
        auto_reply_text = f"Salom men {first_name}ni yordamchisiman. Hozir u yozolmaydi marhamat xabaringizni qoldiring"
        await client.send_message(chat_id=message.chat.id, text=auto_reply_text)

# Run the Pyrogram Client
async def main():
    await app.start()
    await app.idle()
app.run()

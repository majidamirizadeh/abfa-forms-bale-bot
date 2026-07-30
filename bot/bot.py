from bale import Bot, Message
from config import TOKEN
import requests


bot = Bot(TOKEN)

GITHUB_RAW = "https://raw.githubusercontent.com/majidamirizadeh/abfa-forms-bale-bot/main/"


folders = {
    "1": ("دفتر درآمد مشترکین", "forms/daramad"),
    "2": ("دفتر بازرسی مشترکین", "forms/bazrasi"),
    "3": ("دفتر خدمات مشترکین", "forms/khadamat"),
    "4": ("دفتر حسابداری مشترکین", "forms/hesabdari"),
}


menu = """
📂 انتخاب دفتر:

1️⃣ دفتر درآمد مشترکین
2️⃣ دفتر بازرسی مشترکین
3️⃣ دفتر خدمات مشترکین
4️⃣ دفتر حسابداری مشترکین
"""


@bot.event
async def on_ready():
    print("ربات فعال شد")


@bot.event
async def on_message(message: Message):

    if message.text == "/start":
        await message.reply(menu)
        return


    if message.text in folders:

        name, path = folders[message.text]

        await message.reply(
            f"📁 {name}\n\n"
            "فرم‌ها آماده ارسال هستند."
        )

        # فعلا تستی
        pdf_url = GITHUB_RAW + path + "/test.pdf"

        await message.reply(
            "در حال ارسال فایل..."
        )

        await message.send_document(
            pdf_url
        )


bot.run()

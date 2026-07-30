import requests
from config import BALE_TOKEN

API = f"https://tapi.bale.ai/bot{BALE_TOKEN}/"

def send_message(chat_id, text):
    requests.post(
        API + "sendMessage",
        json={
            "chat_id": chat_id,
            "text": text
        }
    )


def get_updates():
    r = requests.get(API + "getUpdates")
    return r.json()


print("ربات فرم‌های آبفا فعال شد")

while True:
    data = get_updates()

    if "result" in data:
        for item in data["result"]:
            try:
                message = item["message"]
                chat_id = message["chat"]["id"]
                text = message.get("text", "")

                if text == "/start":
                    send_message(
                        chat_id,
                        """سلام 👋
فرم مورد نیاز خود را انتخاب کنید:

1️⃣ دفتر درآمد مشترکین
2️⃣ دفتر بازرسی مشترکین
3️⃣ دفتر خدمات مشترکین
4️⃣ دفتر حسابداری مشترکین"""
                    )

            except Exception:
                pass

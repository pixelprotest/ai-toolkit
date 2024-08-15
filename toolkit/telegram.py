from dotenv import load_dotenv
import urllib.parse
import urllib.request
import requests
import os

load_dotenv()
bot_token = os.environ.get('TELEGRAM_LORA_BOT_TOKEN', None)
chat_id = os.environ.get('TELEGRAM_LORA_CHAT_ID', None)

def send_image(image_path, image_caption=""):
    if not bot_token or not chat_id:
        print('--- no telegram bot or chatid env variables have been set up, so skipping')
        return

    data = {
        "chat_id": chat_id,
        "caption": image_caption
    }
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto?{urllib.parse.urlencode(data)}"

    with open(image_path, "rb") as image_file:
        ret = requests.post(url, data=data, files={"photo": image_file})
    return ret.json()

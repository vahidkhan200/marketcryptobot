import os
import requests
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_signal(signal):
    msg = f"""سیگنال جدید:
ارز: {signal['symbol']}
پوزیشن: {signal['position']}
ورود: {signal['entry']}
تارگت ۱: {signal['tp1']}
تارگت ۲: {signal['tp2']}
حد ضرر: {signal['sl']}
لورج: {signal.get('leverage', 'N/A')}
الگو: {signal['pattern']}"""
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

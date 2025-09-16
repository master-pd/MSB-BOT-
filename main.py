#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from telegram import Bot
import time
import random
from datetime import datetime

# ====== Banner ======
print("""
===================================
      🚀 MSB-BOT 🚀
===================================
CREATED TIME: {}
DATE: {}
CREATOR: MAR PD ☠️
===================================
""".format(datetime.now().strftime("%H:%M:%S"), datetime.now().strftime("%d-%m-%Y")))

# ====== Bot Token ======
bot_token = input("Bot Token : ").strip()
bot = Bot(token=bot_token)

# ====== Chat ID ======
chat_id = input(" Chat ID : ").strip()

# ====== Predefined Messages ======
messages = [
    "হাই! কেমন আছো?",
    "আজকের দিনটা কেমন যাচ্ছে?",
    "মজা করছে তো?",
    "কোথায় আছো আজ?",
    "সব ঠিক আছে তো?",
    "যাই হোক মূল কথায় আসি।"
]

# ====== Optional: File Messages ======
file_name = input("MASSAGE FILE  (default skip): ").strip()
if file_name:
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            file_messages = [line.strip() for line in f if line.strip()]
            messages += file_messages
            print(f"✅ {len(file_messages)} টি মেসেজ ফাইল থেকে লোড করা হয়েছে।")
    except FileNotFoundError:
        print(f"⚠️ ফাইল {file_name} পাওয়া যায়নি, শুধু predefined মেসেজ ব্যবহার করা হবে।")

if not messages:
    print("❌ কোনো মেসেজ পাওয়া যায়নি। Exit হচ্ছে।")
    exit()

# ====== Number of Messages ======
try:
    total_count = int(input("মোট কতগুলো মেসেজ পাঠাতে চাও? (উদাহরণ: 1000): "))
except:
    print("ভুল ইনপুট! সংখ্যা দিতে হবে।")
    exit()

# ====== Log Files ======
success_log = "success_log.txt"
fail_log = "fail_log.txt"

# ====== Sending Messages ======
print("🚀 Bot শুরু হলো! প্রতি সেকেন্ডে 2টি করে মেসেজ পাঠানো হবে...")

sent_count = 0

try:
    while sent_count < total_count:
        # প্রতি রাউন্ডে 2টি মেসেজ পাঠানো
        for _ in range(2):
            if sent_count >= total_count:
                break
            msg = random.choice(messages)
            try:
                bot.send_message(chat_id=chat_id, text=msg)
                print(f"[{sent_count+1}/{total_count}] ✅ পাঠানো হয়েছে: {msg}")
                with open(success_log, "a", encoding="utf-8") as log:
                    log.write(f"{datetime.now()} | {msg}\n")
            except Exception as e:
                print(f"[{sent_count+1}/{total_count}] ❌ সমস্যা হয়েছে: {e}")
                with open(fail_log, "a", encoding="utf-8") as log:
                    log.write(f"{datetime.now()} | {msg} | Error: {e}\n")
            sent_count += 1
        time.sleep(1)  # প্রতি সেকেন্ডে 2টি মেসেজ
except KeyboardInterrupt:
    print("\n🛑 Bot বন্ধ করা হলো।")

print(f"✅ সব {sent_count} মেসেজ পাঠানো শেষ।")
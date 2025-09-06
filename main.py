import time
import requests
import schedule
from flask import Flask
from threading import Thread

# بيانات البوت
TOKEN = "8216174167:AAHlAoMrf2BTEQfLhRXK7GJ11yqAtFMaX28"
CHAT_ID = "@win_bettingMa"  # 👈 اسم المستخدم ديال القناة/المجموعة

# صورة + نص
PHOTO_ID = "AgACAgQAAxkBAAMDaLt2SIF0r0N8lc80W9OByp9ZOkcAAuTRMRt3jOFRLgxgK4a4BjoBAAMCAAN5AAM2BA"
MESSAGE_TEXT = """دورييات و البطولات بذات و حتا حنا غدي نبداو في صح .. 💰💰

بذا تانتا معنا في ربح من الكرة القدم 🏟 عندنا فريق يقوم بتحليلات دقيقة و بادوات الذكاء الاصطناعي لكيخلي اننا انخرجو رابحن ب %98

فتح حتى نتا حسابك في منصة   🔗 [1win](https://cutt.ly/1win_registration)  ✅

1️⃣  ـ  اختر طريقة تسجيل 
2️⃣  ـ ادخل رقم الهاتف و بريدك الالكتروني 
3️⃣  ـ ختار كلمة المرور 
4️⃣  ـ دخل الرمز ترويجي :  `1QRQ`

**رمز ترويجي ضروري و مأكد ‼️🎁🎁🎁**

5️⃣  ـ ضغط في التسجيل 

لتحميل تطبيق 1win 
👉 https://cutt.ly/application_1win 👈
"""

# إرسال صورة مع نص
def send_photo(photo_id, caption, parse_mode="Markdown"):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    data = {
        "chat_id": CHAT_ID,
        "photo": photo_id,
        "caption": caption,
        "parse_mode": parse_mode,
        "disable_web_page_preview": False
    }
    requests.post(url, json=data)
    print("✅ تم نشر الرسالة مع الصورة.")

# جدولة النشر يومياً
def schedule_jobs():
    # النشر يومياً مع منتصف الليل 00:00 بتوقيت المغرب
    schedule.every().day.at("00:00").do(send_photo, PHOTO_ID, MESSAGE_TEXT)

    while True:
        schedule.run_pending()
        time.sleep(30)

# Flask (للحفاظ على عمل البوت في Railway أو Replit)
app = Flask('')

@app.route('/')
def home():
    return "✅ البوت يعمل بنجاح"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    Thread(target=run).start()

# تشغيل
keep_alive()
schedule_jobs()

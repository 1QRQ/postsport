import time
import requests
import schedule
from flask import Flask
from threading import Thread

# بيانات البوت
TOKEN = "8216174167:AAHlAoMrf2BTEQfLhRXK7GJ11yqAtFMaX28"
CHAT_ID = "@win_bettingMa"  # 👈 اسم القناة أو المجموعة

# صورة + نص (مع HTML formatting)
PHOTO_ID = "AgACAgQAAxkBAAMDaLt2SIF0r0N8lc80W9OByp9ZOkcAAuTRMRt3jOFRLgxgK4a4BjoBAAMCAAN5AAM2BA"
MESSAGE_TEXT = """دورييات و البطولات بذات و حتا حنا غدي نبداو في صح .. 💰💰

بذا تانتا معنا في ربح من الكرة القدم 🏟 عندنا فريق يقوم بتحليلات دقيقة و بادوات الذكاء الاصطناعي لكيخلي اننا انخرجو رابحن ب %98

فتح حتى نتا حسابك في منصة   🔗 <a href="https://cutt.ly/1win_registration">1win</a> ✅

1️⃣  ـ  اختر طريقة تسجيل 
2️⃣  ـ ادخل رقم الهاتف و بريدك الالكتروني 
3️⃣  ـ ختار كلمة المرور 
4️⃣  ـ دخل الرمز ترويجي :  <code>1QRQ</code>

<b>رمز ترويجي ضروري و مأكد ‼️🎁🎁🎁</b>

5️⃣  ـ ضغط في التسجيل 

لتحميل تطبيق 1win 
👉 https://cutt.ly/application_1win 👈
"""

# إرسال صورة مع نص
def send_photo(photo_id, caption, parse_mode="HTML"):
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
    data = {
        "chat_id": CHAT_ID,
        "photo": photo_id,
        "caption": caption,
        "parse_mode": parse_mode,
        "disable_web_page_preview": False
    }
    r = requests.post(url, data=data)
    print("✅ تم نشر الرسالة مع الصورة." if r.status_code == 200 else r.text)

# جدولة النشر انطلاقاً من لحظة التشغيل
def schedule_jobs():
    # نشر مباشرة عند تشغيل البوت
    send_photo(PHOTO_ID, MESSAGE_TEXT)

    # الحصول على الوقت الحالي
    now = time.strftime("%H:%M")  # مثل "22:15"
    print(f"⏰ البوت سيتكرر يومياً على الساعة: {now}")

    # برمجة النشر يومياً في نفس الساعة
    schedule.every().day.at(now).do(send_photo, PHOTO_ID, MESSAGE_TEXT)

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

# تشغيل Flask + Scheduler مع بعض
if __name__ == "__main__":
    keep_alive()
    Thread(target=schedule_jobs).start()

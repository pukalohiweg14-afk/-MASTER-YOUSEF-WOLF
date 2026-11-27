# 🐺 MASTER YOUSEF WOLF EMPIRE — Panel-Silence

پنل مدیریت VPN بر پایه‌ی **Cloudflare Workers** (Sukot v2.7.0) با رمز جدید، ایدی‌های پشتیبانی، و بنر اعلامیه.

---

## 🔗 آدرس پنل فعال

**https://panel-silence3.panel-silence.workers.dev**

## 🔐 رمز پنل

```
M@st3r_Y0us3f#W0LF!928
```

## 📞 ایدی‌های پشتیبانی

- پشتیبانی اول: **@Kmnbvczx0090**
- پشتیبانی دوم: **@vpnstan2**

## 📣 کانال تلگرام

**https://t.me/vpnstan1**

---

## ✅ آپگریدهای اعمال‌شده

| # | آپگرید | توضیح |
| --- | --- | --- |
| 1 | 🔐 رمز پنل جدید | رمز به `M@st3r_Y0us3f#W0LF!928` تغییر کرد (داخل KV `panel_settings` ذخیره شده) |
| 2 | 📞 ایدی‌های پشتیبانی در فیلد تلگرام | فیلد `telegram` در `panel_settings` به‌روزرسانی شد تا هر دو ایدی پشتیبانی رو نشون بده |
| 3 | 📣 بنر اعلامیه با ایدی پشتیبانی | فیلد `announce` در `wolf_state` با متن «🐺 MASTER YOUSEF WOLF EMPIRE — پشتیبانی: @Kmnbvczx0090 \| @vpnstan2 👑» به‌روزرسانی شد |
| 4 | 🌐 ورکر تازه و پایدار | روی `panel-silence3` مستقر شد با کد اصلی بدون تغییر، از همون KV مشترک استفاده می‌کنه |
| 5 | 🤖 تنظیمات tgBot | آدرس `tgBotUrl` به‌روزرسانی شد تا به ورکر جدید `panel-silence3` اشاره کنه |

---

## 📁 فایل‌های این ریپو

| فایل | توضیح |
| --- | --- |
| `panel-silence-worker.js` | کد ورکر اصلی پنل (Sukot v2.7.0) — آماده deploy |
| `wrangler.toml` | فایل کانفیگ wrangler (با متغیرهای env شامل ایدی‌های پشتیبانی) |
| `update_kv_branding.py` | اسکریپت پایتون برای اعمال آپگریدهای رمز/پشتیبانی/بنر روی KV |
| `.gitignore` | فایل نادیده‌گیری گیت |
| `README.md` | این فایل |

---

## 🚀 راهنمای کامل: از صفر تا پنل آنلاین

### قدم ۱: ساخت ریپو تازه روی گیت‌هاب

چون اکانت قبلی خراب شده، با اکانت جدیدت:

1. برو به **github.com** و وارد شو
2. بالا راست، روی **`+`** کلیک کن → **New repository**
3. اسم بده: `wolf-empire` (یا هر چی دوست داری)
4. ⚠️ حتماً **Private** انتخاب کن (چون توش توکن ربات و UUID هست)
5. تیک **Add a README file** رو نزن (ما خودمون README می‌ذاریم)
6. **Create repository** رو بزن

### قدم ۲: آپلود فایل‌ها

روی صفحه‌ی مخزن جدیدت:

1. روی **`uploading an existing file`** کلیک کن
2. این فایل‌ها رو بکش توش:
   - `panel-silence-worker.js`
   - `wrangler.toml`
   - `update_kv_branding.py`
   - `.gitignore`
   - `README.md`
3. پیام کامت بنویس: `initial panel setup`
4. **Commit changes** رو بزن

> 💡 **راه جایگزین:** اگه آپلود روی گوشی سخته، می‌تونی از فایل `wolf-empire.zip` (که کنار این پوشه‌ست) استفاده کنی. فقط فایل‌ها رو ازش extract کن و دوباره آپلود کن.

### قدم ۳: ویرایش `wrangler.toml` با مقادیر اکانت خودت

اگه می‌خوای روی اکانت Cloudflare خودت دیپلوی کنی، این مقادیر رو ویرایش کن:

```toml
[[kv_namespaces]]
binding = "KV"
id = "KV_NAMESPACE_ID_OWN"  # آیدی KV namespace خودت

[vars]
TG_BOT_TOKEN = "YOUR_TG_BOT_TOKEN"  # توکن ربات تلگرام خودت
UUID = "YOUR_UUID"  # UUID خودت
TG_ADMIN_ID = "YOUR_TG_ADMIN_ID"
PUBLIC_URL = "your-worker.your-subdomain.workers.dev"
```

> ⚠️ اگه فقط می‌خوای از همون پنل فعلی (`panel-silence3`) استفاده کنی و نیازی به دیپلوی مجدد نیست، نیازی به تغییر `wrangler.toml` نیست. فقط فایل‌ها رو روی گیت‌هاب نگه دار برای پشتیبان.

### قدم ۴: دیپلوی ورکر (اگه لازم شد)

```bash
# 1) کلون کن
git clone https://github.com/YOUR_USERNAME/wolf-empire.git
cd wolf-empire

# 2) نصب wrangler
npm i -g wrangler

# 3) لاگین به Cloudflare
wrangler login

# 4) دیپلوی
wrangler deploy
```

### قدم ۵: اعمال آپگریدهای KV (رمز، پشتیبانی، بنر)

اگه ورکر جدید دیپلوی کردی، این اسکریپت رو اجرا کن تا رمز و ایدی‌های پشتیبانی روی KV اعمال بشن:

```bash
# ویرایش متغیرهای CF_TOKEN و ACCOUNT_ID داخل فایل
python3 update_kv_branding.py
```

---

## 🔍 تست پنل

بعد از دیپلوی:

- **آدرس پنل:** `https://panel-silence3.panel-silence.workers.dev`
- **رمز ورود:** `M@st3r_Y0us3f#W0LF!928`
- **چک سلامت:** `https://panel-silence3.panel-silence.workers.dev/api/session`

باید پاسخ JSON با این فیلدها بده:
```json
{
  "authed": false,
  "setup": false,
  "kvBound": true,
  "version": "2.7.0",
  "app": "Sukot",
  "telegram": "https://t.me/Kmnbvczx0090 | https://t.me/vpnstan2",
  "colo": "HKG"
}
```

---

## ⚠️ نکات امنیتی

- 🔒 ریپو رو **حتماً Private** بساز
- 🤫 توکن ربات تلگرام (`TG_BOT_TOKEN`) و UUID هرگز به کسی نده
- 🔄 اگه ریپو public لازم داری، اول مقادیر حساس داخل `wrangler.toml` رو با placeholder جایگزین کن
- 🛡️ توکن Cloudflare (`CF_TOKEN`) داخل `update_kv_branding.py` هست — اگه فایل رو share کردی، اول اون رو پاک کن

---

## 🆘 پشتیبانی

- 📞 **@Kmnbvczx0090**
- 📞 **@vpnstan2**
- 📣 کانال: **https://t.me/vpnstan1**

---

## 📜 اطلاعات نسخه

- **app:**MSTRYOSEF 
  
- **version:** 2.7.0
- **worker name:** `panel-silence3`
- **KV namespace ID:** `2201c97b22f246af9863c188eac94658`
- **Durable Object:** `LiveCounter` (sqlite storage)
- **colo:** HKG (Hong Kong)

---

👑 **MASTER YOUSEF WOLF EMPIRE** 🐺

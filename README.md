# ربات تلگرام پایتون (Polling)

این یک ربات مینیمال تلگرام با Python است که با Long Polling اجرا می‌شود.

## راه‌اندازی سریع

1) از BotFather یک ربات بسازید و توکن بگیرید.

2) فایل `.env.example` را کپی کنید و مقدار توکن را تنظیم کنید:

```bash
cp .env.example .env
```

3) محیط مجازی بسازید و وابستگی‌ها را نصب کنید:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

4) اجرا:

```bash
python telegram_bot/main.py
```

اگر متغیر محیطی `TELEGRAM_BOT_TOKEN` را در محیط تنظیم کرده‌اید، نیازی به `.env` نیست.

## دستورات

- `/start`: شروع
- `/help`: راهنما
- `/ping`: تست پینگ

هر پیام متنی دیگر Echo می‌شود.

## پیکربندی محیط

می‌توانید از `.env` استفاده کنید:

```
TELEGRAM_BOT_TOKEN=123456789:ABCDEF_your_token_here
```

یا در Shell:

```bash
export TELEGRAM_BOT_TOKEN="123456789:ABCDEF_your_token_here"
```

## اجرا با Docker

1) ساخت ایمیج:

```bash
docker build -t telegram-bot .
```

2) اجرا با تعیین توکن در محیط:

```bash
docker run --rm -e TELEGRAM_BOT_TOKEN="123456789:ABCDEF_your_token_here" telegram-bot
```

یا با Docker Compose (از فایل `.env.example` یک `.env` بسازید و توکن را قرار دهید):

```bash
cp .env.example .env
docker compose up --build
```

# WireGuard
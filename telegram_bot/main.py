import os
import sys
import logging
from typing import Final

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None:
        return
    text = (
        "سلام! من یک ربات پایتونی هستم.\n"
        "دستورها:\n"
        "/start — شروع\n"
        "/help — راهنما\n"
        "/ping — تست پاسخگویی"
    )
    await update.message.reply_text(text)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None:
        return
    text = (
        "راهنما:\n"
        "- پیام متنی بفرست تا همون رو برگردونم (echo).\n"
        "- با /ping می‌تونی تست بگیری."
    )
    await update.message.reply_text(text)


async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None:
        return
    await update.message.reply_text("pong ✅")


async def echo_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None or update.message.text is None:
        return
    await update.message.reply_text(update.message.text)


async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None:
        return
    await update.message.reply_text("این دستور رو نمی‌شناسم ✋")


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.exception("Unhandled exception while handling an update", exc_info=context.error)


def main() -> None:
    load_dotenv()
    token: Final[str | None] = os.getenv("TELEGRAM_BOT_TOKEN")

    if not token:
        print(
            "ERROR: متغیر محیطی TELEGRAM_BOT_TOKEN تنظیم نشده.\n"
            "- از BotFather توکن بگیر.\n"
            "- مقدار رو در فایل .env قرار بده یا به صورت محیطی ست کن، مثلا:\n"
            "  export TELEGRAM_BOT_TOKEN=\"123456:ABC...\"",
            file=sys.stderr,
        )
        sys.exit(1)

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("ping", ping))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_message))
    application.add_handler(MessageHandler(filters.COMMAND, unknown_command))

    application.add_error_handler(error_handler)

    logger.info("Bot is starting with long polling...")
    application.run_polling()


if __name__ == "__main__":
    main()


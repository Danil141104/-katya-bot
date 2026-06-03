"""
Зайка Катя — Телеграм бот с Mini App
Запуск: python bot.py
Установка: pip install python-telegram-bot==20.*
"""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

# ── Вставь сюда свои данные ──────────────────────────────────────────────────
import os
BOT_TOKEN = os.environ["BOT_TOKEN"]
GAME_URL   = os.environ["GAME_URL"]
# ─────────────────────────────────────────────────────────────────────────────

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="🐰 Играть!",
            web_app=WebAppInfo(url=GAME_URL)
        )
    ]])
    await update.message.reply_text(
        "Привет! 🌸\nЗдесь живёт зайка Катя — нажми кнопку чтобы начать!",
        reply_markup=keyboard
    )

async def help_cmd(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🐰 Зайка Катя\n\n/start — открыть игру"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    print("Бот запущен! Нажми Ctrl+C чтобы остановить.")
    app.run_polling()

if __name__ == "__main__":
    main()

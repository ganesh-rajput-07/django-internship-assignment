import os
import django
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from django.conf import settings
from asgiref.sync import sync_to_async  # This is the key fix!

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_internship.settings')
django.setup()

from .models import TelegramUser

@sync_to_async
def save_telegram_user(username):
    TelegramUser.objects.get_or_create(telegram_username=username)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.from_user.username
    await save_telegram_user(username)  # Call wrapped function
    await update.message.reply_text(f'Hi {username}, you are now registered!')

def run_bot():
    app = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    print("Bot is running...")
    app.run_polling()

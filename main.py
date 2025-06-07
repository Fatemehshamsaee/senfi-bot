from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

def start(update: Update, context: CallbackContext):
    menu_text = (
        "منوی خدمات:\n"
        "1. ارتباط با شورای صنفی 👥\n"
        "   🔑 آی‌دی: @Civil_senfi\n"
        "   📧 ایمیل: senfi.cie@sharif.edu\n"
        "2. کانال‌های مهم عمرانی 🏗️\n"
        "3. کانال‌های مهم دانشگاه شریف 🎓\n"
        "4. رزرو غذا 🍽️\n"
        "5. فرم‌های مهم دانشجویی 📄\n"
        "7. ارتباط با انجمن علمی 🧪\n"
        "8. ارتباط با نشریه عمران 📰"
    )
    update.message.reply_text(menu_text)

def main():
    TOKEN = os.getenv("BOT_TOKEN")
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

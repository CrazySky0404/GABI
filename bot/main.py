import logging
import os

from handlers import choose_language, language_callback_handler, start_command
from telegram.ext import CallbackQueryHandler, CommandHandler, Updater

TOKEN = os.environ["GABI_TOKEN"]
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Configure automatic restart in case of application or server failure


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("language", choose_language))
    dp.add_handler(CallbackQueryHandler(language_callback_handler, pattern="^(en|uk)$"))
    updater.start_polling()

    # The bot runs until it is stopped manually
    updater.idle()


if __name__ == "__main__":
    main()

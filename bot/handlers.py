import json

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext


# Localization
def load_localizations(file_path):
    with open(file_path, encoding="utf-8") as file:
        return json.load(file)


def get_localization(user_language):
    file_path = f"../locales/{user_language}.json"
    return load_localizations(file_path)


def start_command(update: Update, context: CallbackContext):
    user_language = context.user_data.get("language", "en")  # Default to English
    locs = get_localization(user_language)
    update.message.reply_text(locs["greeting"])
    choose_language(update, context)


def choose_language(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("English", callback_data="en"),
            InlineKeyboardButton("Українська", callback_data="uk"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Please choose your language / Будь ласка, виберіть мову:",
        reply_markup=reply_markup,
    )


def language_callback_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    language_code = query.data
    context.user_data["language"] = language_code
    locs = get_localization(language_code)
    query.edit_message_text(text=locs["language_set"])

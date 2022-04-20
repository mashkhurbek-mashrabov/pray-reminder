import os

from django.db import models

BOT_TOKEN = os.getenv('BOT_TOKEN')
CONFIRMATION_CHANNEL_ID = os.getenv('CONFIRMATION_CHANNEL_ID')
MAIN_CHANNEL_ID = os.getenv('MAIN_CHANNEL_ID')
GREETING_VOICE = os.getenv('GREETING_VOICE')
CHANNEL_PHOTO = os.getenv('CHANNEL_PHOTO')
EXCEPTION_CHANNEL_ID = os.getenv('EXCEPTION_CHANNEL_ID')
PHOTO_STORAGE_CHANNEL = os.getenv('PHOTO_STORAGE_CHANNEL')
CHAT_GROUP_USERNAME = os.getenv('CHAT_GROUP_USERNAME')
# GROUP_CHAT_ID = os.getenv('GROUP_CHAT_ID')

messages = {
    'greeting': '😊 Assalom alaykum, xush kelibsiz! Men sizga kunlik namoz vaqtlarini yuborib tuaraman.',
    'uzbek': '🇺🇿 O`zbek tili',
    'russian': '🇷🇺 Русский',
    'confirm emoji': '✅',
    'decline emoji': '❌',
    'send message': "📤 Xabar jo'natish",
    'main menu': '⏏️ Asosiy menu',
    'back_button': '⬅️ Ortga',
    'cancel': '❌ Bekor qilish',
    'write message': "✍ Xabarni kiriting",
    'confirm message': "Ushbu xabarni tasdiqlaysizmi ?",
    'declined': "❌ Bekor qilindi",
    'confirmed': "✅ Tasdiqlandi",
    'successful': "✅ Yetkazildi : ",
    'unsuccessful': "❌ Yetkazilmadi : ",
    'uz': {
        'language flag': '🇺🇿',
        'back_button': '⬅️ Ortga',
    },

    'ru': {
        'language flag': '🇷🇺',
        'back_button': '⬅️ Ortga',
    }

}


class CallbackData:
    main_menu_button = 'main menu'
    back_button = 'back button'
    confirm = 'confirm'
    decline = 'decline'
    sold_out = 'sold_out'


class BotUserSteps:
    MAIN_MENU = 1
    GET_MSG = 2
    ASK_CONFIRMATION = 3


class BotUserLanguageChoices(models.TextChoices):
    UZBEK = 'uz'
    RUSSIAN = 'ru'


class Moderators:
    admins_id = [
        1004815988,
        1004815988
    ]

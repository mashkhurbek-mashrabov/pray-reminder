import telebot
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from bot.constants import BOT_TOKEN, BotUserSteps, Moderators
from bot.controllers.main import BotController

bot = telebot.TeleBot(BOT_TOKEN)


@csrf_exempt
def webhook_handler(request):
    if request.method == 'POST':
        bot.process_new_updates(
            [telebot.types.Update.de_json(
                request.body.decode("utf-8"))]
        )
        return HttpResponse(status=200)
    else:
        return HttpResponse('.')


@bot.message_handler(commands=['start'])
def start_handler(message):
    controller = BotController(message, bot)
    controller.greeting()


@bot.message_handler(content_types=['text'])
def message_handler(message):
    controller = BotController(message, bot)
    user_step = controller.step
    message_text = message.text
    if message_text == controller.t('back_button'):
        controller.back_reply_button_handler()
    elif message_text == controller.t('main menu'):
        controller.main_menu()
    elif message_text == controller.messages('send message') and message.chat.id in Moderators.admins_id:
        controller.get_msg()
    elif user_step == BotUserSteps.GET_MSG and message.chat.id in Moderators.admins_id:
        controller.ask_confirm_msg()


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(callback):
    controller = BotController(callback, bot)
    user_step = controller.step
    callback_data = callback.data

    if callback_data == 'confirm_msg' and user_step == BotUserSteps.ASK_CONFIRMATION:
        controller.confirm_msg(text=controller.message.message.text)
    elif callback_data == 'decline_msg' and user_step == BotUserSteps.ASK_CONFIRMATION:
        controller.decline_msg()
    elif callback_data == 'back button':
        controller.back_inline_button_handler()
    elif callback_data == 'main menu':
        controller.main_menu()


@bot.message_handler(content_types='contact')
def contact_handler(phone):
    controller = BotController(phone, bot)
    user_step = controller.step


@bot.message_handler(content_types=['location'])
def location_handler(message):
    controller = BotController(message, bot)
    user_step = controller.step


@bot.message_handler(func=lambda message: True, content_types=['photo', 'video', 'audio', 'document'])
def photo_handler(message):
    controller = BotController(message, bot)
    user_step = controller.step

from telebot.types import KeyboardButton, InlineKeyboardButton, ReplyKeyboardRemove

from bot.constants import GREETING_VOICE, BotUserSteps, BotUserLanguageChoices, Moderators
from bot.controllers.base import BaseController
from bot.models import TelegramBotUser


class BotController(BaseController):
    def greeting(self):
        self.sync_user()
        # self.bot.send_voice(chat_id=self.chat_id, voice=GREETING_VOICE)
        self.send_message(message_text=self.messages('greeting'))
        if self.message.chat.id in Moderators.admins_id:
            self.main_menu()

    def back_reply_button_handler(self):
        step = self.step

        if step == BotUserSteps.GET_MSG:
            self.main_menu()

    def back_inline_button_handler(self):
        step = self.step

    def main_menu(self):
        self.sync_user()
        markup = self.reply_markup()
        markup.row(KeyboardButton(text=self.messages('send message')))
        self.send_message(message_text=self.messages('main menu'), reply_markup=markup)
        self.set_step(BotUserSteps.MAIN_MENU)

    def get_msg(self):
        markup = self.reply_markup()
        markup.add(self.back_reply_button)
        self.send_message(message_text=self.messages('write message'), reply_markup=markup)
        self.set_step(BotUserSteps.GET_MSG)

    def ask_confirm_msg(self):
        markup = self.inline_markup()
        markup.row(InlineKeyboardButton(self.messages('decline emoji'), callback_data='decline_msg'),
                   InlineKeyboardButton(self.messages('confirm emoji'), callback_data='confirm_msg'))
        self.send_message(message_text=self.messages('confirm message'), reply_markup=ReplyKeyboardRemove())
        self.send_message(message_text=self.message_text, reply_markup=markup)
        self.set_step(BotUserSteps.ASK_CONFIRMATION)

    def decline_msg(self):
        markup = self.inline_markup()
        markup.add(InlineKeyboardButton(self.messages('declined'), callback_data='None'))
        self.edit_message(message=self.message.message.text, message_id=self.callback_query_id, reply_markup=markup)
        self.main_menu()

    def confirm_msg(self, text):
        all_user = TelegramBotUser.objects.all()
        successful = 0
        unsuccessful = 0
        for user in all_user:
            try:
                self.send_message(message_text=text, chat_id=user.chat_id)
                successful += 1
            except:
                unsuccessful += 1
        markup = self.inline_markup()
        markup.add(InlineKeyboardButton(self.messages('confirmed'), callback_data='None'))
        self.edit_message(message=self.message.message.text, message_id=self.callback_query_id, reply_markup=markup)
        self.send_message(message_text=f"{self.messages('successful')}{successful}\n"
                                       f"{self.messages('unsuccessful')}{unsuccessful}")
        self.main_menu()

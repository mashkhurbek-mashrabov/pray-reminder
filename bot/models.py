from django.db import models

from bot.constants import BotUserLanguageChoices


class TelegramBotUser(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True)
    chat_id = models.CharField(max_length=100, unique=True)
    step = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=32)
    language = models.CharField(max_length=2, null=True, blank=True, choices=BotUserLanguageChoices.choices,
                                default=BotUserLanguageChoices.UZBEK)

    def __str__(self):
        return f'{self.chat_id} - {self.name}'

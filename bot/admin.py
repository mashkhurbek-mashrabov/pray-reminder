from django.contrib import admin

from bot.models import TelegramBotUser


@admin.register(TelegramBotUser)
class TelegramBotUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'chat_id', 'phone_number', 'step', 'language']
    search_fields = ('chat_id', 'phone_number', 'username')
    list_filter = ['language']
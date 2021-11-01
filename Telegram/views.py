import time
from Telegram.models import *
from django.http import HttpResponse
from telegram.ext import Updater
import telegram
from datetime import date


def index(request):
    setting = Setting.objects.get(id=1)
    token = setting.token

    bot = telegram.Bot(token=token)
    today = date.today()

    chat_id = setting.chat_id

    members = Member.objects.filter(date=today)

    for item in members:
        bot.kick_chat_member(
            chat_id=chat_id,
            user_id=item.user_id

        )
    response = HttpResponse("Done")
    return response

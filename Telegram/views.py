import time
from Telegram.models import *
from django.http import HttpResponse
from telegram.ext import Updater
import telegram
from datetime import date


def index(request):
    # token = '2075266445:AAEL05k7urfQ4uGV3Rt-KxuTlI7HxDLc1yc'
    # bot = telegram.Bot(token=token)
    # today = date.today()
    #
    # chat_id = -1001326811432
    # user_id = 1687107831
    #
    # members = Member.objects.filter(date=today)
    # for item in members
    # a = bot.getChatMember(chat_id=chat_id)
    # bot.kick_chat_member(
    #     chat_id=chat_id,
    #     user_id=user_id)
    response = HttpResponse("a")
    return response

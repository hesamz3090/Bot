import time

from django.http import HttpResponse
from telegram.ext import Updater
import telegram


def index(request):
    token = '2075266445:AAEL05k7urfQ4uGV3Rt-KxuTlI7HxDLc1yc'
    bot = telegram.Bot(token=token)
    chat_id = -1001326811432
    user_id = 1687107831
    bot.kick_chat_member(
        chat_id=chat_id,
        user_id=user_id,)
    response = HttpResponse('Done')
    return response

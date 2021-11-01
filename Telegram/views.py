from django.http import HttpResponse
from telegram.ext import Updater
import telegram


def index(request):
    token = '2075266445:AAEL05k7urfQ4uGV3Rt-KxuTlI7HxDLc1yc'
    bot = telegram.Bot(token=token)
    chat_id = 1539258067
    bot.sendMessage(chat_id=chat_id, text='bot_welcome')
    response = HttpResponse('Done')
    return response

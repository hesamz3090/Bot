from django.http import HttpResponse


def index(request):
    response = HttpResponse('Done')
    return response

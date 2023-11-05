from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Request, RequestMessage


def viewing_request(request: HttpRequest) -> HttpResponse:
    """
    Просмотр всех заявок
    """
    context = {
        'requests': Request.objects.all(),
    }
    return render(request, 'nekta_requests/viewing_requests.html', context=context)


def send_message(request: HttpRequest) -> HttpResponse:
    request_id = request.POST.get('request-ID', '')
    context = {
        'requests': Request.objects.all(),
        'request_id': request_id
    }

    if request.method == 'POST':
        message = RequestMessage()
        message.text = request.POST.get('message', '')
        message.request_id = request_id
        message.save()

    return render(request, 'nekta_requests/send_message.html', context=context)


def add_request(request: HttpRequest) -> HttpResponse:
    """
    Добавление заявки
    """
    if request.method == 'POST':
        user = User.objects.get(username='admin')
        req = Request()
        req.title = request.POST.get('req_title', '')
        req.description = request.POST.get('req_description', '')
        req.user = user
        req.save()

    return render(request, 'nekta_requests/add_request.html')


def something(request):
    pass





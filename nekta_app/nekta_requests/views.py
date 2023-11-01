from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Request


def viewing_request(request: HttpRequest):
    """
    Просмотр всех заявок
    """
    context = {
        'requests': Request.objects.all(),
    }
    return render(request, 'nekta_requests/viewing_requests.html', context=context)


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

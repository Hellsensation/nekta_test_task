from django.shortcuts import render
from .models import Request


def nekta_request(request):
    context = {
        'requests': Request.objects.all(),
    }
    return render(request, 'nekta_requests/requests.html', context=context)

from django.urls import path
from .views import nekta_request

appname = 'nekta_requests'


urlpatterns = [
    path('', nekta_request, name='requests'),

    ]

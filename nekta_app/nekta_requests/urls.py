from django.urls import path
from .views import viewing_request, add_request, send_message

appname = 'nekta_requests'


urlpatterns = [
    path('requests/', viewing_request, name='requests'),
    path('add_request/', add_request, name='add_request'),
    path('send_message/', send_message, name='send_message'),

    ]

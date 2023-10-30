from django.urls import path
from .views import viewing_request, add_request

appname = 'nekta_requests'


urlpatterns = [
    path('requests/', viewing_request, name='requests'),
    path('add_req/', add_request, name='add_request'),
    ]

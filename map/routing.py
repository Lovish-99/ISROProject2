# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/action/$', consumers.ChatConsumer.as_asgi()),
]
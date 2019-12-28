from django.contrib import admin
from django.urls import path, include
from .views import Index, SendInvites, ReplyInvites


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('sendIvites', SendInvites.as_view(), name='send_invites'),
    path('replyInvites', ReplyInvites.as_view(), name='reply_invites')
]

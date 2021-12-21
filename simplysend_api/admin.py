from django.contrib import admin
from .models.user import User
from .models.friend_request import Friend_Request
from .models.conversation import Conversation
from .models.message import Message
# Register your models here.
admin.site.register(User)
admin.site.register(Friend_Request)
admin.site.register(Conversation)
admin.site.register(Message)
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from .conversation import Conversation

class Message(models.Model):
    content = models.CharField(max_length=500)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.author} says {self.content}"
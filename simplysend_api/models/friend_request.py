from django.db import models
from .user import User

class Friend_Request(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.from_user} wants to be your friend!"
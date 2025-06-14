from django.contrib.auth.models import User
from django.db import models

class TelegramUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    telegram_username = models.CharField(max_length=255)

    def __str__(self):
        return self.telegram_username

from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    password = models.CharField(max_length=150, verbose_name="пароль")
    number = models.SmallIntegerField(verbose_name="номер", **NULLABLE)
    birthday = models.DateField(default='1900-01-01', verbose_name="дата рождения")
    creation_date = models.DateTimeField(verbose_name="дата создания", auto_now_add=True, editable=False)
    editing_date = models.DateTimeField(verbose_name="дата редактирования", auto_now_add=True, editable=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

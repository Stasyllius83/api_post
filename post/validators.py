from rest_framework import serializers
from rest_framework.serializers import ValidationError
from users.models import User
from datetime import datetime


FORBIDDEN_WORDS = ["ерунда", "глупость", "чепуха"]



def validate_age(value):
    """Функция проверяет, что автор поста достиг возраста 18 лет.

    Args:
        value (int): id пользователя

    Raises:
        serializers.ValidationError: _description_
    """

    author = value["author"]
    birthday = User.objects.get(pk=author.pk).birthday

    age = datetime.now().year - birthday.year - ((datetime.now().month, datetime.now().day) < (birthday.month, birthday.day))
    if age < 18:
        raise serializers.ValidationError("Возраст автора поста должнен быть не младше 18 лет.")


def forbidden_words(value):
    """Функция проверяет, что автор в заголовок не вписал запрещенные слова: ерунда, глупость, чепуха.

    Args:
        value (str): Заголовок поста

    Raises:
        serializers.ValidationError: _description_
    """

    title = value["title"]

    if title.lower() in FORBIDDEN_WORDS:
        raise serializers.ValidationError("В заголовке запрещены слова: ерунда, глупость, чепуха.")

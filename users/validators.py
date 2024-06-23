from rest_framework import serializers
from rest_framework.serializers import ValidationError


DOMAINS_ALLOWED = ["mail.ru", "yandex.ru"]

def validate_password(value):
    """Функция для проверки пароля (должен быть не менее 8 символов, должен включать цифры).

    Args:
        value (str): пароль

    Raises:
        serializers.ValidationError: _description_
    """

    password = value["password"]

    if (not any(character.isdigit() for character in password)) or (len(password) < 8):
        raise serializers.ValidationError("Пароль должен быть не менее 8 символов и должен включать цифры")


def validate_email(value):
    """Функция для проверки почты (разрешены домены: mail.ru, yandex.ru).

    Args:
        value (str): почта

    Raises:
        serializers.ValidationError: _description_
    """

    email = value["email"]

    if DOMAINS_ALLOWED[0] not in email:
        if DOMAINS_ALLOWED[1] not in email:
            raise serializers.ValidationError("Почта должна быть в разрешенных доменах: mail.ru, yandex.ru")

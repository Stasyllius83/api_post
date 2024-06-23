from rest_framework import serializers
from rest_framework.serializers import ValidationError
from users.models import User
from datetime import datetime


FORBIDDEN_WORDS = ["ерунда", "глупость", "чепуха"]



def validate_age(value):

    author = value["author"]
    birthday = User.objects.get(pk=author.pk).birthday
    print(birthday)
    age = datetime.now().year - birthday.year - ((datetime.now().month, datetime.now().day) < (birthday.month, birthday.day))
    if age < 18:
        raise serializers.ValidationError("Возраст автора поста должнен быть не младше 18 лет.")


def forbidden_words(value):

    title = value["title"]

    if title.lower() in FORBIDDEN_WORDS:
        raise serializers.ValidationError("В заголовке запрещены слова: ерунда, глупость, чепуха.")

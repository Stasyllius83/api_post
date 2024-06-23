from rest_framework import serializers
from post.validators import forbidden_words, validate_age
from .models import Post, Comment




class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для пользователя
    """
    class Meta:
        model = Post
        fields = '__all__'
        """
        Дополнительная валидация для сериализатора
        """
        validators = [
        validate_age,
        forbidden_words,
        ]

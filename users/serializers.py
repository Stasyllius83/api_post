from rest_framework import serializers
from users.validators import validate_email, validate_password
from .models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        validators = [
        validate_password,
        validate_email,
        ]

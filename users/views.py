from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from users.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated, IsAdminUser



class UserListAPIView(generics.ListAPIView):
    """Функция для просмотра списка всех пользователей

    Args:
        generics (_type_): _description_
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated | IsAdminUser]


class UserCreateAPIView(generics.CreateAPIView):
    """Функция для создания пользователя

    Args:
        generics (_type_): _description_
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        new_user = serializer.save()
        password = serializer.data["password"]
        new_user.set_password(password)
        new_user.save()


class UserUpdateAPIView(generics.UpdateAPIView):
    """Функция для редактирования пользователя
    Args:
        generics (_type_): _description_
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]

    def perform_update(self, serializer):
        new_user = serializer.save()
        new_user.save()


class UserDestroyAPIView(generics.DestroyAPIView):
    """Функция для удаления пользователя

    Args:
        generics (_type_): _description_
    """
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]

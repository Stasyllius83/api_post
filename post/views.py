from rest_framework import generics
from post.permissions import IsOwner
from post.serializers import CommentSerializer, PostSerializer
from post.models import Post, Comment
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_comment = serializer.save()
        new_comment.author = self.request.user
        new_comment.save()


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [AllowAny]


class CommentUpdateView(generics.UpdateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]


class CommentDestroyView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_post = serializer.save()
        new_post.author = self.request.user
        new_post.save()


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]


class PostUpdateView(generics.UpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]


class PostDestroyView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]

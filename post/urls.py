from django.urls import path
from post.apps import PostConfig
from post.views import CommentCreateAPIView, CommentDestroyView, CommentListAPIView, CommentUpdateView, PostCreateAPIView, PostDestroyView, PostListAPIView, PostUpdateView

app_name = PostConfig.name


urlpatterns = [
    path('comment/create/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('comment/', CommentListAPIView.as_view(), name='comment-list'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDestroyView.as_view(), name='comment-delete'),
    path('post/create/', PostCreateAPIView.as_view(), name='post-create'),
    path('post/', PostListAPIView.as_view(), name='post-list'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDestroyView.as_view(), name='post-delete'),
]

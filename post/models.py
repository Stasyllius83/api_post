from django.db import models
from django.contrib.auth import get_user_model
#from config import settings

NULLABLE = {"null": True, "blank": True}

class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, verbose_name='автор', **NULLABLE)
    text = models.TextField(verbose_name='текст')
    creation_date = models.DateTimeField(verbose_name="дата создания", auto_now_add=True, editable=False)
    editing_date = models.DateTimeField(verbose_name="дата редактирования", auto_now_add=True, editable=False)

    def __str__(self) -> str:
        return f'{self.author}'

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    text = models.TextField(verbose_name='текст')
    picture = models.ImageField(upload_to='blog/static/img/', verbose_name='изображение', **NULLABLE)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, verbose_name='автор', **NULLABLE)
    comments = models.ManyToManyField(Comment, verbose_name='комментарии', default=None)
    creation_date = models.DateTimeField(verbose_name="дата создания", auto_now_add=True, editable=False)
    editing_date = models.DateTimeField(verbose_name="дата редактирования", auto_now_add=True, editable=False)

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"

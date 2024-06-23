from django.contrib import admin
from post.models import Comment, Post
from django.urls import reverse
from django.utils.http import urlencode




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'creation_date', 'editing_date')
    list_display_links = ['author', ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'picture', 'author', 'creation_date', 'editing_date', 'view_author_link')
    list_filter = ('creation_date',)
    list_display_links = ['title', ]

    def view_author_link(self, obj):
        from django.utils.html import format_html

        url = (
            reverse("admin:users_user_changelist")
            + "?"
            + urlencode({"post__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} </a>', url, obj.author)
    view_author_link.short_description = "Ссылка на автора"


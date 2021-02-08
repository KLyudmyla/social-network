
from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ["title", "author", "likes"]
    search_fields = ["title"]
    list_filter = ["title", "author"]
    save_on_top = True


admin.site.register(Post, PostAdmin)

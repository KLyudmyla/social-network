
from django.contrib import admin
from .models import Like


class LikeAdmin(admin.ModelAdmin):
    model = Like
    list_display = ["like", "post", "user"]
    search_fields = ["post", "user"]
    list_filter = ["post", "user"]
    save_on_top = True


admin.site.register(Like, LikeAdmin)

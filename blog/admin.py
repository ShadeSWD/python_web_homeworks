from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_filter = ('created_at',)
    search_fields = ('name',)

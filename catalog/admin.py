from django.contrib import admin
from catalog.models import Category, Product, Contacts, Post, Theme


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category_name')
    search_fields = ('category_name', )


@admin.register(Theme)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'theme_name')
    search_fields = ('theme_name', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'price', 'category')
    list_filter = ('category', )
    search_fields = ('product_name', 'description')


@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'post_name', 'theme')
    list_filter = ('theme', 'created_at')
    search_fields = ('product_name', 'theme')


@admin.register(Contacts)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'country', 'itn', 'address')
    search_fields = ('tin', 'country')

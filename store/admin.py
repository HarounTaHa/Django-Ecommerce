from django.contrib import admin

# Register your models here.


from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price', 'is_stock', 'created', 'updated']
    list_filter = ['is_stock', 'is_active']
    list_editable = ['price', 'is_stock']
    prepopulated_fields = {'slug': ('title', )}

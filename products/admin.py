from django.contrib import admin
from .models import Category, Product, Image, ProductAttribute, Tag

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ProductAttributeInline]
    list_display = ['title', 'price', 'category']
    search_fields = ['title', 'category__title', 'tags__name']




admin.site.register(Product, ProductAdmin)

admin.site.register(Category)
admin.site.register(Tag)


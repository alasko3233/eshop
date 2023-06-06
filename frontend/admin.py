from django.contrib import admin

# Register your models here.
#Creation d'un super-utilisateur
from .models import Category, Product
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'created_at', 'updated_at']
    # list_filter = ['name', 'created_at', 'updated_at']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}

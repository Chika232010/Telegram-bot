from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']           
    prepopulated_fields = {'slug': ('name',)} 
    search_fields = ['name']                  
    ordering = ['name']                   
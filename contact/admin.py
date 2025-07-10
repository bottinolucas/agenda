from django.contrib import admin
from contact.models import Contact, Category

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display= 'id', 'first_name', 'last_name', 'email', 'category'
    ordering='id',
    search_fields= 'id', 'first_name', 'last_name'
    list_per_page=10
    list_max_show_all=200

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display= 'name',
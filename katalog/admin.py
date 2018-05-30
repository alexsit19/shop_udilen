from django.contrib import admin
from .models import Categories, Products

# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"alias": ("name",)}

admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Products)





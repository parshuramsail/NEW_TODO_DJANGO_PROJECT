from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'date']

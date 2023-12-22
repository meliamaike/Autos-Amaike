# autosapp/admin.py
from django.contrib import admin
from autosapp.models import Auto

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ['modelo', 'anio', 'precio', 'tipo']
    list_filter = ['tipo']





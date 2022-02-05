from django.contrib import admin
from .models import Service
# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'created')

admin.site.site_header = "Cronos Admin Site"
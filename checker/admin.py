from django.contrib import admin

from .models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('owner', 'file', 'status', 'created_at', 'updated_at',)
    search_fields = ('owner',)

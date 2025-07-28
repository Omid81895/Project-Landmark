from django.contrib import admin
from .models import Landmark, Comment, Tag
# Register your models here.
class LandmarkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created', 'images']
    list_display_links = ['id']
    ordering = ['created']
    list_filter = ['created']
    search_fields = ['name', 'description']
    list_editable = ['name', 'description', 'images']

admin.site.register(Comment)
admin.site.register(Landmark,LandmarkAdmin)
admin.site.register(Tag)

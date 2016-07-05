from django.contrib import admin
from collection.models import Story

class StoryAdmin(admin.ModelAdmin):
    model = Story
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Story, StoryAdmin)

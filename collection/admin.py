from django.contrib import admin
from collection.models import Post

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Post, PostAdmin)

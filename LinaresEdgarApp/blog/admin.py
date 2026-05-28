from django.contrib import admin
from .models import Post, Autor, Tag
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("titol",)}
    
admin.site.register(Post, PostAdmin)
admin.site.register(Autor)
admin.site.register(Tag)

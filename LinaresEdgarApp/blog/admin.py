from django.contrib import admin
from .models import Posts, Autors, Tag
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    pass

admin.site.register(Posts, PostAdmin)
admin.site.register(Autors)
admin.site.register(Tag)

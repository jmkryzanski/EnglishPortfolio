from django.contrib import admin
from .models import Post, Contact

admin.site.register(Post)
admin.site.register(Contact)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

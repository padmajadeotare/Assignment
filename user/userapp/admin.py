from django.contrib import admin
from .models import User,Post

class UserAdmin(admin.ModelAdmin):
    list_display=['username']

admin.site.register(User,UserAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display=['user']

admin.site.register(Post,PostAdmin)


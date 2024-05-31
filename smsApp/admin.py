from django.contrib import admin
from .models import UserInfo,user

class userAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname","email","phone","date")
admin.site.register(UserInfo, userAdmin)

class useradmin(admin.ModelAdmin):
    list_display = ("username","firstname","lastname","email","phone","password")
admin.site.register(user, useradmin)
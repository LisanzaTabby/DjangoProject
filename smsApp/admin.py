from django.contrib import admin
from .models import UserInfo

class userAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname","email","phone","date")
admin.site.register(UserInfo, userAdmin)
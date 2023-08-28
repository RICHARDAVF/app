from django.contrib import admin
from .models import User

class AdminUser(admin.ModelAdmin):
    list_display = ('username','last_name', 'first_name', 'dni', 'email')

admin.site.register(User, AdminUser)

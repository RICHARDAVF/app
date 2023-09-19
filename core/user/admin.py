from django.contrib import admin
from .models import User,Empresa,Puesto,Unidad

class AdminUser(admin.ModelAdmin):
    list_display = ('username','last_name', 'first_name', 'dni', 'email')
admin.site.register(User, AdminUser)

class AdminEmpresa(admin.ModelAdmin):
    list_display = ('ruc',"razon_social")
admin.site.register(Empresa,AdminEmpresa)

class AdminUnidad(admin.ModelAdmin):
    list_display = ('unidad',"empresa")
admin.site.register(Unidad,AdminUnidad)

class AdminPuesto(admin.ModelAdmin):
    list_display = ('unidad',"puesto","direccion")
admin.site.register(Puesto,AdminPuesto)
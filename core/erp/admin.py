from django.contrib import admin

from core.erp.models import CargoTrabajador

# Register your models here.
class AdminCargoView(admin.ModelAdmin):
    list_display = ('id','cargo')
admin.site.register(CargoTrabajador, AdminCargoView)

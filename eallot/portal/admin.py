from django.contrib import admin
from .models import Service, EDC, Service_Grouping

# Register your models here.

admin.site.register(EDC)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = ['name', 'remarks']


@admin.register(Service_Grouping)
class SGAdmin(admin.ModelAdmin):

    list_display = ['serviceNumber', 'servicePassword', 'serviceZone', 'serviceGroup']

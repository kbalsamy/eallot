from django.contrib import admin
from .models import Service, EDC, Service_Grouping, GeneratorReadings

# Register your models here.

admin.site.register(EDC)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = ['name', 'remarks']


@admin.register(Service_Grouping)
class SGAdmin(admin.ModelAdmin):

    list_display = ['serviceNumber', 'servicePassword', 'serviceZone', 'serviceGroup']

@admin.register(GeneratorReadings)
class GRAdmin(admin.ModelAdmin):

    list_display = ['consumerID', 'companyName', 'netUnitsC1', 'netUnitsC2', "netUnitsC3", "netUnitsC4", "netUnitsC5"]

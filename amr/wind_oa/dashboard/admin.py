from django.contrib import admin
from .models import Customer, EDCModel, ServiceGroup, Readings
# Register your models here.


admin.site.register(Customer)
admin.site.register(EDCModel)
admin.site.register(Readings)


@admin.register(ServiceGroup)
class ServiceGroupAdmin(admin.ModelAdmin):

    list_display = ('serviceNumber', 'edc', 'customer',)
    list_filter = ('edc', 'customer',)

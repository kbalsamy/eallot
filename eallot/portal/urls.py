from django.urls import path, re_path
from portal.views import router, addService, deleteService, servicesMapping, serviceUpdateView, serviceDeleteView, displayServiceView

app_name = 'portal'

urlpatterns = [path('service', router, name='service'),
               path('service/add', addService, name='sgadd'),
               path('service/delete', deleteService, name='sgdelete'),
               path('service/mapping', servicesMapping, name='servicemapping'),
               path('service/lists', displayServiceView, name="servicedisplay"),
               path('service/update', serviceUpdateView, name='serviceupdate'),
               path('service/servicedelete', serviceDeleteView, name='servicedelete'),
               ]

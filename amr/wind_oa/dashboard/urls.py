from django.urls import path, include
from .views import mainView, downloadView, readingView

app_name = 'dashboard'

urlpatterns = [path('', mainView, name='home'),
               path('download', downloadView, name='dbconnect'),
               path('readings', readingView, name='readings'), ]

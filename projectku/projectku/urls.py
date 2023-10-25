from django.contrib import admin
from django.urls import path
from appku.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('home/', home, name='home'),


]
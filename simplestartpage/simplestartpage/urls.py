from django.contrib import admin
from django.urls import path
import startpage.views as views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
]

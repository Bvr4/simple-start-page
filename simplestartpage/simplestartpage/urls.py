from django.contrib import admin
from django.urls import path
import startpage.views as views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-ligne/', views.add_ligne, name='add-ligne'),
    path('add-lien/', views.add_lien, name='add-lien'),
    path('admin/', admin.site.urls),
]

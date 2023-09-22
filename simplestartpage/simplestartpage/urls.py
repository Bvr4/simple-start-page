from django.contrib import admin
from django.urls import path
import startpage.views as views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-ligne/', views.add_ligne, name='add-ligne'),
    path('add-lien/', views.add_lien, name='add-lien'),
    path('delete-lien/<int:lien_pk>', views.delete_lien, name='delete-lien'),
    path('delete-ligne/<int:ligne_pk>', views.delete_ligne, name='delete-ligne'),
    path('admin/', admin.site.urls),
]

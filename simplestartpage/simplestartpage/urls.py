from django.contrib import admin
from django.urls import path
import startpage.views as views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-ligne/', views.add_ligne, name='add-ligne'),
    path('add-lien/', views.add_lien, name='add-lien'),
    path('delete-lien/<int:lien_pk>', views.delete_lien, name='delete-lien'),
    path('delete-ligne/<int:ligne_pk>', views.delete_ligne, name='delete-ligne'),
    path('move-lien-up/<int:lien_pk>', views.move_lien_up, name='move-lien-up'),
    path('move-lien-down/<int:lien_pk>', views.move_lien_down, name='move-lien-down'),
    path('edit-lien/<int:lien_pk>', views.edit_lien, name='edit-lien'),
    path('lien/<int:lien_pk>', views.lien, name='lien'),
    path('admin/', admin.site.urls),
]

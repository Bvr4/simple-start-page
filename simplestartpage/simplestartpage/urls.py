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
    path('move-ligne-up/<int:ligne_pk>', views.move_ligne_up, name='move-ligne-up'),
    path('move-ligne-down/<int:ligne_pk>', views.move_ligne_down, name='move-ligne-down'),
    path('edit-lien-form/<int:lien_pk>', views.edit_lien_form, name='edit-lien-form'),
    path('lien/<int:lien_pk>', views.lien, name='lien'),
    path('add-lien-form/<int:ligne_pk>', views.add_lien_form, name='add-lien-form'),
    path('add-lien-ctrl/<int:ligne_pk>', views.add_lien_ctrl, name='add-lien-ctrl'),
    path('admin/', admin.site.urls),
]

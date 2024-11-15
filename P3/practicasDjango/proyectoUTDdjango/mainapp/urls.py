from django.urls import path
from . import views

urlpatterns = [
    path('inicio/',views.index, name='inicio'),
    path('',views.index, name='inicio'),
    path('acercade/',views.about, name='acercade'),
    path('mision/',views.mision, name='mision'),
    path('vision/',views.vision, name='vision'),

]
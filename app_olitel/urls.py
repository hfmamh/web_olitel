
from django.urls import path
#now import the views.py file into this code
from . import views

urlpatterns=[
  path('',views.index),
  path('formulario_nombre',views.formulario_nombre),
  path('formulario_3',views.formulario_3)
]
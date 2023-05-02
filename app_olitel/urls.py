
from django.urls import path
#now import the views.py file into this code
from . import views

urlpatterns=[
  path('',views.index),
  path('formulario_nombre',views.formulario_nombre),
  path('formulario_3',views.formulario_3),
  path('formulario_4',views.formulario_4),
  path('form_widgets',views.form_widgets),
  path('form_modelo',views.form_modelo),
  path('crear_producto',views.crear_producto),
  path('formset_vista',views.formset_vista),
]
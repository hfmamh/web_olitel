from django.db import models
import base64

# Create your models here.

class modelo_1(models.Model):
        # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add = True)
    #img = models.ImageField(upload_to = "images/")
  
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.title
    

class productos(models.Model):
    producto = models.CharField(max_length=200)
    codigo = models.IntegerField(null=True)
    categoria = models.CharField(max_length=50,null=True)
    precio = models.FloatField(null=True)
    unidad =models.CharField(max_length=10,null=True)

class cotizaciones(models.Model):
    codigo = models.TextField(null=True)
    creacion = models.DateTimeField(null=True)
    descripcion = models.TextField(null=True)
    cotizacion = models.TextField()
    

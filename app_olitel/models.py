from django.db import models

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
    id_producto = models.IntegerField(null=True)
    producto = models.CharField(max_length=200)
    precio = models.FloatField(null=True)
from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    nombre_usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email

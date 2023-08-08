from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Aceite(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    uso = models.TextField()
    imagen = models.ImageField(upload_to='aceites', null=True, blank=True)
    def __str__(self):
        return f'Nombre: {self.nombre} - Descripcion: {self.descripcion} - Uso: {self.uso}'

class Accesorios(models.Model):
    art = models.IntegerField()
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    uso = models.TextField()

    def __str__(self):
        return f'Artiículo nro: {self.art} -Nombre: {self.nombre} - Descripción: {self.descripcion} - Uso: {self.uso}'
    
        

class AromaTerapia(models.Model):
    art = models.IntegerField()
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    uso = models.TextField()

    def __str__(self):
        return f'Artiículo nro: {self.art} -Nombre: {self.nombre} - Descripción: {self.descripcion} - Uso: {self.uso}'



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.date}"

class Avatar(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"



    
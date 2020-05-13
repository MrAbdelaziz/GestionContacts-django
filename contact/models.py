from django.db import models

# Create your models here.

class Contact(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    tel = models.IntegerField(max_length=100)
    email=models.EmailField(max_length=255)
    profession = models.CharField(max_length=100)
    user = models.OnetoOneFiled()
    def __str__(self):
        return self.email
class user(models.Model):
    nom = models.CharField(max_length=100)
    login = models.EmailField(max_length=255)
    password = models.CharField(max_length=20)
    date = models.DateField(auto_created=True)
    def __str__(self):
        return self.nom
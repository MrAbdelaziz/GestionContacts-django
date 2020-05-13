# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
# Create your models here.
#  nom, adresse, ville, numéro de téléphone,
# email, profession …
# create contact model
class Contact(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    tel = models.IntegerField()
    email = models.EmailField(max_length=255)
    profession = models.CharField(max_length=100)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    def __str__(self):
        return  self.email
class User(models.Model):
    nom = models.CharField(max_length=100)
    login = models.EmailField(max_length=255)
    password = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.login
class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    def __str__(self):
        return self.nom
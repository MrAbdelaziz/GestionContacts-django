from re import search

from django.contrib import admin
from contact.models import *

class contactModel(admin.ModelAdmin):
    list_display = ('nom','adresse','tel','email')
    list_filter = ('nom','tel')
    search_fields = ('nom',)
    ordering = ('tel',)

admin.site.register(User)
admin.site.register(Contact,contactModel)
admin.site.register(Categorie)


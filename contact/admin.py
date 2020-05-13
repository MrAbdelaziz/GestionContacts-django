from django.contrib import admin
from contact.models import *

class contactModel(admin.ModelAdmin):
    list_display = ('nom','adresse','tel','email')
    list_filter = ('nom','tel')

admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Categorie)


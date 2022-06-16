from django.contrib import admin
from ProyectoCoderApp.models import *
# Register your models here.
class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('nombre','edad','fecha_de_nacimiento')
    
admin.site.register(Familiar,FamiliarAdmin)




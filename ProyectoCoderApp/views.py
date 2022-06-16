from django.shortcuts import render
from ProyectoCoderApp.models import *


def crear_familia (request):
    familia = Familiar.objects.all()
    return render(request,"index.html",{"familia":familia})




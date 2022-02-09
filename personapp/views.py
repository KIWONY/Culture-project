from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def nice_world(request):
    return render(request,"personapp/nice_world.html")      #dobi/personapp/templates/personapp/nice_world.html
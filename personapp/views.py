from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from personapp.models import NiceWorld


def nice_world(request):
    if request.method == "POST":

        temp = request.POST.get("nice_world_input")
        new_nice_world = NiceWorld()        #models에서 정의한 NiceWorld의 새로운 객체
        new_nice_world.text = temp
        new_nice_world.save()               #db에 저장 중

        return render(request,"personapp/nice_world.html", context={"nice_world_output": new_nice_world})   #객체를 내보냄
    #dobi/personapp/templates/personapp/nice_world.html
    else:
        return render(request,"personapp/nice_world.html", context={"text" : "GET METHODS!!!!!!!"})


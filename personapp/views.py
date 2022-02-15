from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from personapp.decorators import account_ownership_required
from personapp.forms import AccountUpdateForm
from personapp.models import NiceWorld
from profileapp.decorators import profile_ownership_required

has_ownership= [account_ownership_required, login_required]


#함수형 view를 사용할 때의 사용자 인증 여부 확인
@login_required
def nice_world(request):
    if request.method == "POST":

        temp = request.POST.get("nice_world_input")
        new_nice_world = NiceWorld()        #models에서 정의한 NiceWorld의 새로운 객체
        new_nice_world.text = temp
        new_nice_world.save()               #db에 저장 중

        nice_world_list = NiceWorld.objects.all()
        return HttpResponseRedirect(reverse("personapp:nice_world"))        #personapp 내부에 있는 nice_world로 재접속
        # return render(request,"personapp/nice_world.html", context={"nice_world_list": nice_world_list})   #객체를 내보냄
        #dobi/personapp/templates/personapp/nice_world.html
    else:
        nice_world_list = NiceWorld.objects.all()
        return render(request,"personapp/nice_world.html", context={"nice_world_list": nice_world_list})



# user는 장고에서 제공하는 템플릿 어디에서든 사용이 가능한, 요청을 보내는 유저의 객체

class AccountCreateView(CreateView):        #import
    model = User                            #장고에서 기본제공, ctrl+b 눌러서 소스코드 확인, import
    form_class = UserCreationForm           #기본제공, import
    success_url = reverse_lazy("personapp:nice_world")      #class와 function의 파이썬에서 불러와지는 방법의 차이(reverse, reverse_lazy)
    template_name = "personapp/create.html"                 #회원가입할 때 보이는 html


# CreateView 때는 form이랑 redirect를 정해줘야 했지만 DetailView는 model과 시각화 할 template만 요함
class AccountDetailView(DetailView):        #import
    model = User                            #장고에서 기본 제공, import
    context_object_name = "target_user"       #다른 유저가 내 페이지에 들어왔을 때 그 유저의 정보가 아닌 내 정보를 보여주기 위해 설정
    template_name = "personapp/detail.html"



@method_decorator(profile_ownership_required, "get" )  #일반 function이 사용하는 decorator를 method에 사용할 수 있도록 변환함.
@method_decorator(profile_ownership_required, "post" )
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm       #이 form을 forms.py에서 커스텀마이징(아이디 수정불가의 기능을 만들기 위한 작업)
    success_url = reverse_lazy("personapp:nice_world")
    template_name = "personapp/update.html"
    context_object_name = "target_user"




@method_decorator(has_ownership, "get" )
@method_decorator(has_ownership, "post" )
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy("personapp:login")
    template_name = "personapp/delete.html"
    context_object_name = "target_user"

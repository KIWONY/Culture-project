from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = "target_profile"
    form_class = ProfileCreationForm                                    #forms파일에서 생성했던.
    success_url = reverse_lazy("personapp:nice_world")
    template_name = "profileapp/create.html"



    # 아래의 form은 forms.py에서 생성한 ProfileCreationForm
    # form_valid 메서드는 유저가 보낸 모든 입력을 검증하고, 검증이 완료 된 이후 실행되는 메서드
    def form_valid(self, form):
        #커스텀마이징(오버라이딩?)
        temp_profile = form.save(commit=False)      #commit을 False로 설정함으로써 실제 db에 반영이 되지않음.
        temp_profile.user = self.request.user       #유저데이터를 request를 보낸 user로 정한다.
        temp_profile.save()
        return super().form_valid(form)


@method_decorator(profile_ownership_required, "get" )
@method_decorator(profile_ownership_required, "post" )
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = "target_profile"
    form_class = ProfileCreationForm                                    #forms파일에서 생성했던.
    success_url = reverse_lazy("personapp:nice_world")
    template_name = "profileapp/update.html"

















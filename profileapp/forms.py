from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:                                         #장고 제공
        model = Profile
        fields = ["image", "nickname", "message"]           #models.py의 class Profile에서 설정한 field
        #user를 field에 설정하지않은 이유: client에서가 아닌 서버에서 구현하여 본인이 아닌 user가 접근하여 이용하는 것을 막기위함
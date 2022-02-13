from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:                                         #장고 제공
        model = Profile
        fields = ["image", "nickname", "message"]           #models.py의 class Profile에서 설정한 field
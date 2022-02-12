# UserCreateionForm 을 커스텀마이징

from django.contrib.auth.forms import UserCreationForm


class AccountUpdateForm(UserCreationForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        # ------------------------------------------여기까지는 UserCreationForm 과 같은 form

        self.fields["username"].disabled = True     #username(= id 값)을 비활성화
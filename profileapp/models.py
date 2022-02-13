from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    #1:1매칭 - 이 profile의 주인 누군지 정해줌, profile과 user를 연결 => OneToOneField
    # User객체와 연결
    # on_delete => 연결된 User객체가 없어질 때 삭제될 때
    # Cascade => 이 profile로 삭제되도록.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    image = models.ImageField(upload_to="profile/", null=True)     # 경로 : media/profile/

    #unique를 true로 설정하면서 profile객체는 하나밖에 설정하지 못하도록 함
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)











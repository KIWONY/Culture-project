from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="subscription")
    project = models.ForeignKey(Project,on_delete=models.CASCADE, related_name="subscription")

#한 쌍이 유일하게 존재하도록. user와 구독한 project가 1:1로 대응
    class Meta:
        unique_together = ("user","project")




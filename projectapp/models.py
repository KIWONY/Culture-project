from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Project(models.Model):

    title = models.CharField(max_length=10, null= False)
    image = models.ImageField(upload_to="project/" , null = False)

    description = models.TextField(max_length=100, null=True)

    create_at = models.DateField(auto_now =True, null = False)

    #project를 찾을 때 Project.pk값과 그 값에 해당하는 title이 순서대로 나오게 함
    def __str__(self):
        return f"{self.pk} : {self.title}"








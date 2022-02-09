from django.db import models

# Create your models here.

class NiceWorld(models.Model):
    text = models.CharField(max_length=255, null= False)

    # 명령어 python manage.py makemigrations
    #       python manage.py migrate
from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    phone_num = models.CharField(verbose_name='Номер телефона',max_length=80)
    avatar = models.ImageField(verbose_name='Аватар',upload_to='users/')
    bio = models.TextField(verbose_name='Биография')
    created_at = models.TimeField()




# Create your models here.

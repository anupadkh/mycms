from django.db import models

# Create your models here.

class FormUser(models.Model):
    username = models.CharField('Username', max_length=20)
    password = models.CharField('Password', max_length=70)

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Modarator(models.Model):
    m_id = models.IntegerField(primary_key=True)
    m_role = models.CharField(max_length=150)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
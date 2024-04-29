from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ServiceProvider (models.Model):
    sp_id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length = 100)
    cv = models.FileField(upload_to='', storage=None, max_length=100)
    photo = models.ImageField(upload_to='', height_field=None, width_field=None, max_length=100,default="")
    p_num = models.IntegerField()
    nid = models.IntegerField()
    sp_rating = models.FloatField(max_length = 4)
    ex = models.FileField(upload_to='', storage=None, max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
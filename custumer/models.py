from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    c_id = models.IntegerField(primary_key=True)
    location = models.TextField(max_length = 50)
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,default="")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
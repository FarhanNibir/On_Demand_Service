from django.db import models

# Create your models here.
class Services (models.Model):
    s_id = models.IntegerField(primary_key=True)
    s_name = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
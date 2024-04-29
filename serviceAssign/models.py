from django.db import models
from django.db import models
from booking_info.models import booking_info
# Create your models here.
class ServiceAssign(models.Model):
    sa_id = models.IntegerField(primary_key=True)
    b_id = models.ForeignKey(booking_info,on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now=False,auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False,auto_now_add=False)
    status = models.CharField(max_length=15)
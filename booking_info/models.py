from django.db import models
from services.models import Services
from custumer.models import Customer
from serviceProvider.models import ServiceProvider 

# Create your models here.
class booking_info(models.Model):
    b_id = models.IntegerField(primary_key=True)
    s_id = models.ForeignKey(Services,on_delete=models.CASCADE)
    c_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    sp_id = models.ForeignKey(ServiceProvider,on_delete=models.CASCADE)
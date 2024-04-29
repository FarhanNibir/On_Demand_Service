from django.db import models
from serviceAssign.models import ServiceAssign
from custumer.models import Customer
from serviceProvider.models import ServiceProvider 

# Create your models here.
class Rating (models.Model):
    r_id = models.IntegerField(primary_key=True)
    rating = models.FloatField()
    sp_id = models.ForeignKey(ServiceProvider,on_delete=models.CASCADE)
    c_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    sa_id = models.ForeignKey(ServiceAssign,on_delete=models.CASCADE)

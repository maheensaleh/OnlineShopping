from home.models import BasicProduct
from django.db import models
# Create your models here.


class Mobile(BasicProduct):

    product_name=None
    product_descr = models.TextField(max_length=1000,default='N.A')
    product_model = models.CharField(max_length=500,default='N.A')
    product_image = models.ImageField(upload_to="Mobile/images",default='N.A')

    def __str__(self):
        return self.product_model








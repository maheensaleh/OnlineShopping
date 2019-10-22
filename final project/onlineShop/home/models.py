from django.db import models


'''Any employee or any other staff member will inherit this basic class'''


class BasicPerson(models.Model):

    name = models.CharField(max_length=40, default='')
    contact = models.IntegerField(default=0)
    address = models.CharField(max_length=100, default='')
    NIC_No = models.IntegerField(default=0)
    email_id = models.EmailField(max_length=100, default='')


'''BasicProduct is an abstract class. Django will not create any database table for it.
Every poduct from every category will be abstracted form this class'''


class BasicProduct(models.Model):

    product_name = models.CharField(max_length=50, default='')
    product_brand = models.CharField(max_length=40, default='')
    product_model=models.CharField(max_length=50, default='')
    product_descr = models.TextField(max_length=2000, default='')
    product_price = models.IntegerField(default=0)
    product_quantity = models.IntegerField(default=0)

    def __str__(self):    # overloading
        return self.product_name

    class Meta:
        abstract = True









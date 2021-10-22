from django.db import models

from shop.models import *
# Create your models here.
class cartlist(models.Model):
    cart_id=models.CharField(max_length=250,unique=True)
    date_added=models.DateField(auto_now_add=True)
    class Meta:
        db_table='cart'
        ordering=('date_added',)
    def __str__(self):
        return self.cart_id

class items(models.Model):
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)
    class Meta:
        db_table='items'
    def sub_total(self):
        return self.product.price*self.quan
    def __str__(self):
        return self.product

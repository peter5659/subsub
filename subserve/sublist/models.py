from django.db import models
from store.models import Store
from menu.models import Menu
from customer.models import Customer
from django.contrib.auth.models import User

class Subscribes(models.Model):
     id = models.AutoField(primary_key = True, default=0)
     user_id=models.ForeignKey(Customer, on_delete=models.CASCADE)
     store_id=models.ForeignKey(Store, on_delete=models.CASCADE)
     menu_id=models.ForeignKey(Menu, on_delete=models.CASCADE)
     start_date=models.DateTimeField(auto_created=True)   
     end_date=models.DateTimeField(auto_created=True)
     total=models.IntegerField()
     cycle=models.IntegerField()
     remain=models.IntegerField()
     last_used=models.DateTimeField(auto_created=True, null=True)
     purchased=models.DateTimeField(auto_created=True)
     purchased_type=models.IntegerField()

     def __str__(self) :
          return str(self.user_id) + "-" + str(self.store_id) + "-" + str(self.menu_id)
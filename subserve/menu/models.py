from django.db import models
from django.contrib.auth.models import User
from store.models import Store
# Create your models here.
class Menu(models.Model):
    store_id=models.ForeignKey(Store, on_delete=models.CASCADE)
    menu_id=models.IntegerField(primary_key=True)
    description=models.CharField(max_length=45)
    price=models.IntegerField(null = True)
    photo=models.CharField(max_length=45, null=True)
    allergic=models.CharField(max_length=45, null = True)
    subscribers=models.IntegerField(null = True)
    cycle=models.IntegerField(null = True)
    count=models.IntegerField(null = True)
    last_subscribers=models.IntegerField(null = True)
    discount=models.IntegerField(null = True)
    in_event=models.BooleanField(null = True)
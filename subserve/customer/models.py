from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True, default=0)
    name=models.CharField(max_length=45, null=True)
    phone=models.CharField(max_length=45, null=True)
    marketing_email=models.BooleanField(null= True)   
    marketing_sms=models.BooleanField(null= True)
    barcode=models.IntegerField(null= True)
    purchasing_type=models.IntegerField(null=True)
    auto_extension=models.BooleanField(null = True)
    locality=models.IntegerField(null = True)
    recent_search_keywords=models.CharField(max_length=45, null=True)
    recent_viewed=models.CharField(max_length=45, null=True)
    profile=models.CharField(max_length=45, null = True)
    address=models.CharField(max_length=45)
    birthday=models.DateTimeField()
    sex=models.BooleanField(null = True)
    certified=models.BooleanField(null = True)
from django.db import models
from django.contrib.auth.models import User
from unixtimestampfield.fields import UnixTimeStampField
#from django.contrib.auth.hashers import make_password      hashed를 위해 import

# Create your models here.
class User(models.Model):
    id=models.IntegerField(primary_key=True)
    pw=models.CharField(max_length=45)  #hashed처리?
    email=models.CharField(max_length=45)  #EmailField 사용?
    phone=models.CharField(max_length=45, null=True)
    marketing_email=models.BooleanField()   
    marketing_sms=models.BooleanField()
    joined_date=models.DateTimeField(auto_now_add=True)
    barcode=models.IntegerField()
    pusrchasing_type=models.IntegerField(null=True)
    auto_extension=models.BooleanField()
    loaclity=models.IntegerField()
    recent_search_keywords=models.CharField(max_length=45, null=True)
    recent_viewed=models.CharField(max_length=45, null=True)
    profile=models.CharField(max_length=45)     #path추가
    birthday=models.DateTimeField(null=True)
    name=models.CharField(max_length=45, null=True)
    sex=models.BooleanField()
    certified=models.BooleanField()


class Store(models.Model):
    id=models.IntegerField(primary_key=True)
    longitude=models.DecimalField(max_digits=30, decimal_places=20)
    latitude=models.DecimalField(max_digits=30, decimal_places=20)
    address=models.CharField(max_length=45)
    photo=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)        #path
    subscribers=models.IntegerField()
    rank=models.IntegerField()
    is_premium=models.BooleanField()
    description=models.CharField(max_length=45, null=True)
    sns1=models.CharField(max_length=45, null=True)
    sns2=models.CharField(max_length=45, null=True)
    phone=models.CharField(max_length=45)
    running_time=models.CharField(max_length=45)
    break_time=models.CharField(max_length=45)
    closed_on=models.CharField(max_length=15)
    num_menu=models.IntegerField()
    locality=models.IntegerField()
    comment=models.CharField(max_length=45)
    category=models.IntegerField()


class Manager(models.Model):
    manager_id=models.IntegerField(primary_key=True)
    id=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    password=models.CharField(max_length=45)       #hashed
    phone=models.CharField(max_length=45)
    alarm_sms=models.BooleanField()
    alarm_push=models.NullBooleanField()


class Menu(models.Model):
    store_id=models.ForeignKey(Store, on_delete=models.CASCADE)
    menu_id=models.IntegerField(primary_key=True)
    description=models.CharField(max_length=45)
    price=models.IntegerField()
    photo=models.CharField(max_length=45, null=True)
    #photo에 char, path 처리
    allergic=models.CharField(max_length=45)
    subscribers=models.IntegerField()
    cycle=models.IntegerField()
    count=models.IntegerField()
    last_subscribers=models.IntegerField()
    discount=models.IntegerField()
    in_event=models.BooleanField()

class Reviews(models.Model):
    review_id=models.IntegerField(primary_key=True)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    store_id=models.ForeignKey(Store, on_delete=models.CASCADE)
    menu_id=models.ForeignKey(Menu, on_delete=models.CASCADE)
    content=models.TextField()
    photo=models.CharField(max_length=45, null=True)  #photo에 char?
    rank=models.IntegerField()

class Subscribes(models.Model):
    id = models.IntegerField(primary_key = True)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)  #관계정의필드..
    store_id=models.ForeignKey(Store, on_delete=models.CASCADE)
    menu_id=models.ForeignKey(Menu, on_delete=models.CASCADE)
    start_date=UnixTimeStampField(auto_created=True)   #timestamp...
    end_date=UnixTimeStampField(auto_created=True)
    total=models.IntegerField()
    cycle=models.IntegerField()
    remain=models.IntegerField()
    last_used=UnixTimeStampField(auto_created=True)
    purchased=UnixTimeStampField(auto_created=True)
    purchased_type=models.IntegerField()

class QnA(models.Model):
    article_id=models.IntegerField(primary_key=True)
    upload_date=models.DateTimeField(auto_now_add=True)
    editted_date=models.DateTimeField(auto_now=True)
    content=models.TextField()
    #content=models.Charfield(max_length=45)
    watched=models.IntegerField()

class Notice(models.Model):
    article_id=models.IntegerField(primary_key=True)
    upload_date=models.DateTimeField(auto_now_add=True)
    editted_date=models.DateTimeField(auto_now=True)
    content=models.TextField()
    #content=models.Charfield(max_length=45)
    watched=models.IntegerField()
    locality=models.IntegerField()

class Wishlist(models.Model):
    id=models.IntegerField(Reviews, on_delete=models.CASCADE, primary_key = True)
    store_id=models.ForeignKey(Store, on_delete=models.CASCADE)
    menu_id=models.ForeignKey(Menu, on_delete=models.CASCADE)

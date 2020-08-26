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
    marketing_email=models.BoleanField()   
    marketing_sms=models.BoleanField()
    joined_date=models.DateTimeField(auto_now_add=True)
    barcode=models.IntegerField()
    pusrchasing_type=models.IntegerField(null=True)
    auto_extension=models.BoleanField()
    loaclity=models.IntegerField()
    recent_search_keywords=models.CharField(max_length=45, null=True)
    recent_viewed=models.CharField(max_length=45, null=True)
    profile=models.CharField(max_length=45)     #path추가
    birthday=models.DateTimeField(null=True)
    name=modles.CharField(max_length=45, null=True)
    sex=models.BoleanField()
    certified=models.BoleanField()


class Store(models.Model):
    id=models.IntegerField(primary_key=True)
    longitude=models.DecimalField(max_digits=30, decimal_places=20)
    latitude=models.DecimalField(max_digits=30, decimal_places=20)
    address=models.CharField(max_length=45)
    photo=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)        #path
    subscribers=models.IntegerField()
    rank=models.IntegerField()
    is_premium=models.BoleanField()
    description=models.CharField(max_length=45, null=True)
    sns1=models.CharField(max_length=45, null=True)
    sns2=models.CharField(max_length=45, null=True)
    phone=models.CharField(max_length=45)
    running_time=models.CharField(max_length=45)
    break_time=models.CharField(max_length=45)
    closed_on=models.CharField()
    num_menu=models.IntegerField()
    locality=models.IntegerField()
    comment=models.CharField(max_length=45)
    category=models.IntegerField()


class Manager(modles.Model):
    manager_id=models.IntegerField(primary_key=True)
    id=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    password=models.CharField(max_length=45)       #hashed
    phone=models.Charfield(max_length=45)
    alarm_sms=models.BoleanField()
    alarm_push=models.NullBoleanField()


class Reviews(models.Model):
    review_id=models.IntegerField(primary_key=True)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    store_id=models.ForeignKey(Store, on_delete=models.CASCADE)
    menu_id=models.ForeignKey(Menu, on_delete=models.CASCADE)
    content=models.TextField()
    photo=models.Charfield(max_length=45, null=True)  #photo에 char?
    rank=models.IntegerField()

class Menu(models.Model):
    store_id=models.ForeignKey(Menu, on_delete=models.CASCADE, primary_key=True)
    menu_id=models.IntegerField(primary_key=True)
    description=models.Charfield(max_length=45)
    price=models.IntegerField()
    photo=models.Charfield(max_length=45, null=True)
    #photo에 char, path 처리
    allergic=models.CharField(max_length=45)
    subscribers=models.IntegerField()
    cycle=models.IntegerField()
    count=models.IntegerField()
    last_subscribers=models.IntegerField()
    discount=models.IntegerField()
    in_event=models.BoleanField()

class Subscribes(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)  #관계정의필드..
    store_id=models.ForeignKey(Store, on_delete=models.CASCADE, primary_key=True)
    menu_id=models.ForeignKey(Menu, on_delete=models.CASCADE, primary_key=True)
    start_date=UnixTimestampField(auto_created=True)   #timestamp...
    end_date=UnixTimestampField(auto_created=True)
    total=models.IntegerField()
    cycle=models.IntegerField()
    remain=models.IntegerField()
    last_used=UnixTimestampField(auto_created=True)
    purchased=UnixTimestampField(auto_created=True)
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

class Wishlist(modles.Nodel):
    id=models.ForeignKey(Reviews, on_delete=models.CASCADE, primary_key=True)
    store_id=models.ForeignKey(Store, on_delete=models.CASCADE)
    menu_id=models.ForeignKey(Menu, on_delete=models.CASCADE)

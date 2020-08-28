from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:storeID>/detail', views.detail, name="detail"),
    path('<int:storeID>/detail', views.purchasing, name="purchasing")
]
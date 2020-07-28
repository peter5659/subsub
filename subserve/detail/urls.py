from django.urls import path, include
from . import views

import main.views

urlpatterns = [
    path('', views.detail, name='detail')
]

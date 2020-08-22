from django.contrib import admin
from django.urls import path, include
import main.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.main, name="main")
]


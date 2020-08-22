from django.contrib import admin
from django.urls import path, include
import main.urls
from user import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.main, name="main"),
    path('user/', include('user.urls'))
]


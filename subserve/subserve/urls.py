from django.contrib import admin
from django.urls import path, include
import main.urls
import detail.urls
from user import views
from detail import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.main, name="main"),
    path('search/', main.views.search, name="search"),
    path('mylocation/', main.views.mylocation, name="mylocation"),
    path('user/', include('user.urls')),
    path('store/', include ('detail.urls'))
]


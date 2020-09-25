from django.contrib import admin
from django.urls import path, include
import main.urls
import detail.urls
from customer import views
from detail import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.main, name="main"),
    path('login/', main.views.login, name="login"),
    path('search/', main.views.search, name="search"),
    path('mylocation/', main.views.mylocation, name="mylocation"),
    path('customer/', include('customer.urls')),
    path('store/', include ('detail.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

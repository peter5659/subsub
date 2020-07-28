from django.contrib import admin
from django.urls import path, include

import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main', main.views.main, name='main'),
    path('', main.views.index, name='index'),
    # path('user/', include('user.urls')),
    path('detail/', include ('detail.urls'))
]


from django.contrib import admin
from django.urls import path, include
import junkfood


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('junkfood.urls')),
]

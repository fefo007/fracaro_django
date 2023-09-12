
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('imagine-and-travel/',include('AppPython.urls'))
]

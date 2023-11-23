
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('base.urls')),  # Include your app's URLs for the empty path
    path('admin/', admin.site.urls),
]

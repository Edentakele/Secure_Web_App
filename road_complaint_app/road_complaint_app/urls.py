from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('complaints.urls')),
     # Other URL patterns
    path('', include('complaints.urls')),
]

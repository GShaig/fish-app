from django.contrib import admin
from django.urls import path, include
from fish.views import DataUploadView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fish.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

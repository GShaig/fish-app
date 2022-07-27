from django.urls import path, include
from fish.views import DataUploadView

urlpatterns = [
    path('', DataUploadView.as_view(), name="home"),
]
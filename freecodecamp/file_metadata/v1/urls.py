from django.urls import path, include
from file_metadata.v1 import views as file_metadata_views

urlpatterns = [
    path(r'api/file/upload',
         file_metadata_views.FileUplpoadDetail.as_view(), name='FileUplpoadDetail'),
]

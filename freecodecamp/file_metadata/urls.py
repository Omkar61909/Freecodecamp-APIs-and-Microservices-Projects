from django.urls import path, include

urlpatterns = [
	path(r'', include('file_metadata.v1.urls'))
]
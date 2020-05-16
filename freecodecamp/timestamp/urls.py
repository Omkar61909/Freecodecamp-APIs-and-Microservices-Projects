from django.urls import path, include

urlpatterns = [
	path(r'', include('timestamp.v1.urls'))]
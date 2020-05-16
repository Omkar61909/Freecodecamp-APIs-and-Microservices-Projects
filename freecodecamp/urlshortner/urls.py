from django.urls import path, include

urlpatterns = [
	path(r'', include('urlshortner.v1.urls'))]
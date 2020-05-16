from django.urls import path, include

urlpatterns = [
	path(r'', include('request_header_parser.v1.urls'))

]
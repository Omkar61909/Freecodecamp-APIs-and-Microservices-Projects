from django.urls import path,include
from request_header_parser.v1 import views


urlpatterns = [   
	path(r'api/whoami/', views.RequestHeaderParserDataDetail.as_view(), name='RequestHeaderParserDataDetail')
]
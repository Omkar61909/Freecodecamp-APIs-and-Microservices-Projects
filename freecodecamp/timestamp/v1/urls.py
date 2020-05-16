from django.urls import path, include
from timestamp.v1 import views as app_views

urlpatterns = [   
	path(r'api/timestamp/<str:datetime>',
         app_views.TimestampDetail.as_view(), name='TimestampDetail'),
	path(r'api/timestamp/',
		app_views.TimestampDetail.as_view(), name='TimestampDetail')]
from django.urls import path, include
from urlshortner.v1 import views as urlshortner_views

urlpatterns = [
    path(r'api/shorturl/new',
         urlshortner_views.URLShortnerDetail.as_view(), name='URLShortnerDetail'),
    path(r'api/shorturl/<str:endpoint>',
         urlshortner_views.redirect_view, name='redirect_view'),
]

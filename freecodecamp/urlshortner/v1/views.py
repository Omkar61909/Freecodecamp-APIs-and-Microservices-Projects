from django.shortcuts import redirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from urlshortner.v1 import serializers as urlshortner_serializer
from urlshortner import models as urlshortner_models

class URLShortnerDetail(APIView):

    def post(self, request, *args, **kwargs):
        data = dict(request.data)
        serializer = urlshortner_serializer.URLShortnerDataSerializer(
            data=data)
        if serializer.is_valid():
            return Response(serializer.perform_tasks_and_get_data(), status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_200_OK)


def redirect_view(request, *args, **kwargs):
    url_shortner_object = urlshortner_models.URLShortnerData.objects.filter(shortened_url_endpoint=kwargs['endpoint']).first()
    original_url = url_shortner_object.original_url
    response = redirect(original_url)
    return response

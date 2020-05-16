from django.shortcuts import redirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# from urlshortner.v1 import serializers as urlshortner_serializer
# from urlshortner import models as urlshortner_models


from rest_framework.parsers import JSONParser, FileUploadParser


class FileUplpoadDetail(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, *args, **kwargs):
        data = dict()
        data['size'] = request.data.get('file').size
        data['type'] = request.data.get('file').content_type
        data['name'] = request.data.get('file').name
        return Response(data, status=status.HTTP_200_OK)

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from timestamp.v1 import serializers as app_serializer

class TimestampDetail(APIView):

	def get(self, request, *args, **kwargs):
		data = dict(request.data, **kwargs)
		serializer = app_serializer.TimestampSerializer(data=data)
		if serializer.is_valid():
			return Response(serializer.get_data() ,status=status.HTTP_200_OK)
		return Response({'error': 'Invalid Date'}, status=status.HTTP_200_OK)
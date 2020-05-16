from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from request_header_parser.v1.services import request_header_parser_data_service


class RequestHeaderParserDataDetail(APIView):
	def get(self, request, *args, **kwargs):
		data = request_header_parser_data_service.RequestHeaderParserData(request).get_data()
		return Response(data, status=status.HTTP_200_OK)
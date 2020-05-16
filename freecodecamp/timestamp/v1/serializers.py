from rest_framework import serializers
from timestamp.v1.services import timestamp_data_service

class TimestampSerializer(serializers.Serializer):
	datetime = serializers.CharField(required=False)

	def get_data(self):
		data = timestamp_data_service.TimestampData(self.validated_data).get_data()
		return data
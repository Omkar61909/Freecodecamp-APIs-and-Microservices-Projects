from rest_framework import serializers
from urlshortner.v1.services import url_shortner_data_service

class URLShortnerDataSerializer(serializers.Serializer):
	original_url = serializers.URLField()

	def perform_tasks_and_get_data(self):
		data = url_shortner_data_service.URLShortnerData(self.validated_data).perform_tasks_and_get_data()
		return data



class UserExerciseLogDataSerializer(serializers.Serializer):
	user_id = serializers.CharField()
	from_date = serializers.DateField(required=False)
	to_date = serializers.DateField(required=False)
	limit = serializers.IntegerField(required=False)

	def get_data(self):
		data =  url_shortner_data_service.UserExerciseLogData(self.validated_data).get_data()
		return data
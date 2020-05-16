from rest_framework import serializers
from exercise_tracker.v1.services import exercise_tracker_data_service

class ExerciseCreateUserSerializer(serializers.Serializer):
	user_name = serializers.CharField(max_length=256)

	def perform_tasks_and_get_data(self):
		data = exercise_tracker_data_service.ExerciseUser(self.validated_data).perform_tasks_and_get_data()
		return data

class UserExerciseLogDataSerializer(serializers.Serializer):
	user_id = serializers.CharField()
	exercise_description = serializers.CharField()
	exercise_duration = serializers.IntegerField()
	exercise_date = serializers.DateField()

	def perform_tasks_and_get_data(self):
		data = exercise_tracker_data_service.UserExerciseActionLog(self.validated_data).perform_tasks_and_get_data()
		return data


class UserExerciseDataSerializer(serializers.Serializer):
	user_id = serializers.CharField()
	to_date = serializers.DateField(required=False)
	from_date = serializers.DateField(required=False)
	limit = serializers.IntegerField(required=False)

	def get_data(self):
		data = exercise_tracker_data_service.UserExerciseActionLog(self.validated_data).get_data()
		return data
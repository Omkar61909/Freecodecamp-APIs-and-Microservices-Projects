from django.shortcuts import redirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from exercise_tracker.v1 import serializers as exercise_tracker_serializer


class ExerciseCreateUserDetail(APIView):
    def post(self, request, *args, **kwargs):
        data = dict(request.data)
        serializer = exercise_tracker_serializer.ExerciseCreateUserSerializer(
            data=data)
        if serializer.is_valid():
            return Response(serializer.perform_tasks_and_get_data(), status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        data = {
            'user_id': request.query_params.get('user_id'),
            'from_date': request.query_params.get('from_date'),
            'to_date': request.query_params.get('to_date'),
            'limit': request.query_params.get('limit')
        }
        serializer = exercise_tracker_serializer.UserExerciseDataSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.get_data(), status=status.HTTP_200_OK)   
        return Response({'error': serializer.errors}, status=status.HTTP_200_OK)

class UserExerciseActionLogDetail(APIView):
    def post(self, request, *args, **kwargs):
        data = dict(request.data)
        serializer = exercise_tracker_serializer.UserExerciseActionLogSerializer(
            data=data)
        if serializer.is_valid():
            return Response(serializer.perform_tasks_and_get_data(), status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_200_OK) 
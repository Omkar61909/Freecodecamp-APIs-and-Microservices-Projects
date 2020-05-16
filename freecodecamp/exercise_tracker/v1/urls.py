from django.urls import path, include
from exercise_tracker.v1 import views as exercise_tracker_views

urlpatterns = [
    path(r'api/exercise/new_user',
         exercise_tracker_views.ExerciseCreateUserDetail.as_view(), name='ExerciseCreateUserDetail'),
    path(r'api/exercise/add',
    	exercise_tracker_views.UserExerciseActionLogDetail.as_view(), name='UserExerciseActionLogDetail'),
    path(r'api/exercise/log',
         exercise_tracker_views.ExerciseCreateUserDetail.as_view(), name='URLShortnerDetail')

]

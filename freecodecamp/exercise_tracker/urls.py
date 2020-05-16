from django.urls import path, include

urlpatterns = [
	path(r'', include('exercise_tracker.v1.urls'))
]
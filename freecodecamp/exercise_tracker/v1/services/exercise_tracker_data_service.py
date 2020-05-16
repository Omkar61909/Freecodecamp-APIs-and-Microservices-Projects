import copy
import datetime
import operator
from functools import reduce
from django.db.models import Q
from exercise_tracker import models as exerise_tracker_models


class ExerciseUser(object):
    def __init__(self, data):
        self.data = data
        self.user_name = self._user_name()

    def _user_name(self):
        user_name = ''
        if self.data.get('user_name'):
            user_name = self.data['user_name'] 
        return user_name

    def _exercise_user_id(self):
        exercise_user_id = None
        exercise_user_object, is_created = exerise_tracker_models.User.objects.get_or_create(
            user_name=self.user_name)
        if is_created:
            exercise_user_id = exercise_user_object.user_id
        return exercise_user_id

    def perform_tasks_and_get_data(self):
        data = dict()
        exercise_user_id = self._exercise_user_id()
        if exercise_user_id:
            data['user_name'] = self.user_name
            data['user_id'] = exercise_user_id
        else:
            data['error'] = 'Username already taken'
        return data


class UserExerciseActionLog(object):
    def __init__(self, data):
        self.data = data
        self.user_name = self._user_name()

    def _user_name(self):
        user_name = None
        user_exercise_object = exerise_tracker_models.User.objects.filter(
            user_id=self.data.get('user_id')).first()
        if user_exercise_object:
            user_name = user_exercise_object.user_name
        return user_name

    def _create_exercise_log(self):
        exerise_tracker_models.ExerciseUserLog.objects.create(**self.data)

    def perform_tasks_and_get_data(self):
        data = dict()
        if self.user_name:
            self._create_exercise_log()
            data = copy.deepcopy(self.data)
            data['user_name'] = self.user_name
        else:
            data['error'] = 'User does not exist'
        return data


MODEL_FIELD_MAP = {
    'ExerciseUserLog': {
        'fields_key_map': {
            'exercise_description': 'description',
            'exercise_duration': 'duration',
            'exercise_date': 'date',
        }
    }
}


class UserExerciseActionLog(object):
    def __init__(self, data):
        self.data = data
        self.user_name = self._user_name()
        self.user_exercise_logs = self._user_exercise_logs()

    def _change_keys(self, input_dict, key_map):
        output_dict = dict()
        for model_key, data_key in key_map.items():
            if input_dict.get(model_key):
                output_dict[data_key] = input_dict[model_key]
        return output_dict

    def _user_name(self):
        user_name = None
        if self.data.get('user_id'):
            user_id = self.data['user_id']
            model_values = exerise_tracker_models.User.objects.filter(
                user_id=user_id).values('user_name').first()
            if model_values and model_values.get('user_name'):
                user_name = model_values.get('user_name')
        return user_name

    def _query_list(self):
        queries = {
            'user_id': "user_id",
            'from_date': "exercise_date__gte",
            'to_date': 'exercise_date__lte'
        }
        predicates = []
        for field, value in self.data.items():
            if value and field in queries:
                predicates.append((queries[field], value))
        q_list = [Q(x) for x in predicates]
        return q_list

    def _user_exercise_logs(self):
        user_exercise_logs = list()
        if self.user_name and self.data.get('user_id'):
            query_list = self._query_list()
            model_values = exerise_tracker_models.ExerciseUserLog.objects.filter(
                reduce(operator.and_, query_list)).values(*MODEL_FIELD_MAP['ExerciseUserLog']['fields_key_map'].keys())
            for model_data in model_values:
                output_dict = self._change_keys(
                    model_data, MODEL_FIELD_MAP['ExerciseUserLog']['fields_key_map'])
                user_exercise_logs.append(output_dict)
        return user_exercise_logs

    def get_data(self):
        data = dict()
        data = {
            '_id': self.data.get('user_id'),
            'user_name': self.user_name,
            'count': len(self.user_exercise_logs),
            'log': self.user_exercise_logs
        }
        return data

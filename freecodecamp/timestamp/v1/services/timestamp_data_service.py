import re
import datetime


class TimestampData(object):
    def __init__(self, data):
        self.data = data
        self.datetimestamp = self._datetimestamp()

    def _datetimestamp(self):
        datetimestamp = datetime.datetime.now()
        if self.data.get('datetime'):
            try:
                datetime_string = self.data['datetime']
                r = re.compile('^\d{4}-\d{2}-\d{2}')
                if r.match(datetime_string):
                    datetimestamp = datetime.datetime.strptime(
                        datetime_string, '%Y-%m-%d')
                else:
                    datetimestamp = datetime.datetime.utcfromtimestamp(
                        int(datetime_string))
            except Exception as e:
                datetimestamp = None
        return datetimestamp

    def _timestamp_data(self):
        if self.datetimestamp:
            timestamp_data = {
                'unix': self.datetimestamp.strftime("%s"),
                'utc': str(self.datetimestamp)
            }
        else:
            timestamp_data = {
                'error': 'Invalid Date'
            }
        return timestamp_data

    def get_data(self):
        data = dict()
        data = self._timestamp_data()
        return data

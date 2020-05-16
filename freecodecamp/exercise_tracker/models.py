import random
import string
from django.db import models
from django.db import IntegrityError


class User(models.Model):
    user_id = models.CharField(
        max_length=16, blank=True, editable=False, unique=True, primary_key=True)
    user_name = models.CharField(max_length=256, blank=True, null=True, db_index=True)

    def generate_random_alphanumeric(self, string_size):
    	return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(string_size))

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = self.generate_random_alphanumeric(9)
        success = False
        failures = 0
        while not success:
            try:
                super(User, self).save(*args, **kwargs)
            except IntegrityError:
                failures += 1
                if failures > 5:
                    raise
                else:

                    self.user_id = self.generate_random_alphanumeric(9)
            else:
                success = True

    class Meta(object):
        db_table = "exercise_user"

    def __unicode__(self):
        return "%s" % (str(self.user_id))


class ExerciseUserLog(models.Model):
	user = models.ForeignKey('User', on_delete=models.CASCADE)
	exercise_description = models.TextField(null=True, blank=True)
	exercise_duration = models.IntegerField(null=True, blank=True)
	exercise_date = models.DateField(null=True, blank=True)

	class Meta(object):
		db_table = "exercise_user_log"

	def __unicode__(self):
		return "%s" % (str(self.user_id))
from django.db import models


class URLShortnerData(models.Model):
    url_id = models.AutoField(primary_key=True)
    original_url = models.TextField(db_index=True, blank=True, null=True)
    shortened_url_endpoint = models.CharField(
        db_index=True, max_length=256, blank=True, null=True)

    class Meta(object):
        db_table = "url_shortner_data"

    def __unicode__(self):
        return "%s" % (str(self.url_id))

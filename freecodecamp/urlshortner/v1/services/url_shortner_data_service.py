from urlshortner import models as urlshortner_models

class URLShortnerData(object):
    def __init__(self, data):
        self.data = data
        self.original_url = self._original_url()

    def _original_url(self):
    	original_url = ''
    	if self.data.get('original_url'):
    		original_url = self.data['original_url']
    	return original_url

    def _url_shortner(self):
    	url_shortner_object, is_created = urlshortner_models.URLShortnerData.objects.get_or_create(original_url=self.original_url)
    	if is_created:
    		url_shortner_object.shortened_url_endpoint = url_shortner_object.url_id
    		url_shortner_object.save()
    	return url_shortner_object

    def perform_tasks_and_get_data(self):
        data = dict()
        url_shortner_object = self._url_shortner()
        data = {
        	'original_url': url_shortner_object.original_url,
        	'short_url': url_shortner_object.shortened_url_endpoint
        }
        return data

class RequestHeaderParserData(object):
	def __init__(self, request):
		self.request = request

	def get_data(self):
		data =  dict()
		data['ipaddress'] = self.request.META.get('REMOTE_ADDR')
		data['language'] = self.request.META.get('LANGUAGE')
		data['software'] = self.request.META.get('HTTP_USER_AGENT')
		return data
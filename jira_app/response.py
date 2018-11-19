from django.http import JsonResponse


class ResponseMiddleware(object):
    SUCCESS_STATUS = [200, 201]

    def __init__(self, get_response=None):
        self.get_response = get_response
        super(ResponseMiddleware,self).__init__()

    def __call__(self, request):
        response = None
        if not response:
            response = self.get_response(request)
        if has_attribute(self, 'process_response'):
            response = self.process_response(request, response)
            return response

    def process_response(self, request, response):

        if response.status_code not in self.SUCCESS_STATUS:
            return response

        data = {}

        data['data'] = response.data
        data['notification'] = {}
        data['notification']['Done'] = 'Response was Sent Successfully'
        data['notification']['type'] = 'Success'
        data['notification']['message'] = 'Sending Response To Get Success'
        data['notification']['status'] = response.status_code

        return JsonResponse(data, status=response.status_code)


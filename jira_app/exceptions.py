from django.http import JsonResponse


class ExceptionMiddleware(object):

    def __init__(self, get_response=None):
        self.get_response = get_response
        super(ExceptionMiddleware, self).__init__()

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        try:
            exception.url
        except Exception as e:
            if 'Error' in e.message:
                exception.message = 'NOT_FOUND'
                exception.url = (['Clue', 'http://www.nexiilabs.com/support/flas'],)
                exception.HTTP_status = 404
            else:
                exception.message = 'Internal Server Error'
                exception.payload = (['Clue', e.message],)
                exception.HTTP_status = 500

        response = {}
        response['data'] = exception.message
        response['notification'] = {}
        response['notification'] = dict(exception.url or ())
        response['notification']['message'] = 'Failed to respond'
        response['notification']['type'] = 'error'
        response['notification']['status'] = exception.HTTP_status

        return JsonResponse(response, status=exception.HTTP_status)
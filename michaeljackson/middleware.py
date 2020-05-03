from michaeljackson.data import get_random_info


class MJMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Michael-Jackson'] = get_random_info()
        return response

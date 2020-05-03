from django_michaeljackson.data import get_random_info


class MJMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_response(self, request, response):
        response['X-Michael-Jackson'] = get_random_info()
        return response

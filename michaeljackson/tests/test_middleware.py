from django.test import TestCase, modify_settings

from michaeljackson.tests.setup import configure_django

configure_django()


@modify_settings(MIDDLEWARE={
    'append': 'michaeljackson.middleware.MJMiddleware'
})
class MJMiddlewareTestCase(TestCase):
    def test_response(self):
        response = self.client.get('/')
        self.assertIn('x-michael-jackson', response._headers)

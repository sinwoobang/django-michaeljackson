from django.conf.urls import url

from michaeljackson.tests.views import DummyView

urlpatterns = [
    url(r'^$', DummyView.as_view()),
]


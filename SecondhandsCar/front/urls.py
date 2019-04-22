from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^$', IdexView.index,name="index"),
    url(r'test/', IdexView.test,name="test"),
]
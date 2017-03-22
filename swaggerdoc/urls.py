from django.conf.urls import url
from .views import DocIndexView


urlpatterns = [
    url(r'^$', DocIndexView.as_view(), name='doc-index')
]

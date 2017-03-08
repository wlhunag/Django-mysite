from django.conf.urls import url, include
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/', include([
        url(r'^detail/$', views.DetailView.as_view(), name='detail'),
        url(r'^results/$', views.ResultsView.as_view(), name='results'),
        url(r'^vote/$', views.vote, name='vote'),

    ]))
]

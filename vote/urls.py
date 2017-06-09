from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^vote', views.votepage, name='votepage'),
    url(r'^count', views.count, name='count'),
    url(r'^settings', views.settings, name='settings'),
    url(r'^results', views.results, name='results'),
    url(r'^choose', views.choose, name='choose'),
    url(r'^set', views.voter, name='set'),
    url(r'^loadsave', views.loadsave, name='loadsave'),
]

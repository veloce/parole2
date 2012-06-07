from django.conf.urls import patterns, url

urlpatterns = patterns('paroles.views',
    url(r'^$', 'index'),
)

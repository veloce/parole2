from django.conf.urls import patterns, url

urlpatterns = patterns('paroles.views',
    url(r'^$', 'index'),
    url(r'^parole/(\d{4})/(\d{2})/(\d{2})/([-\w]+)$', 'parole'),
)

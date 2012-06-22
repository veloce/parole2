from django.conf.urls import patterns, url

urlpatterns = patterns('paroles.views',
    url(r'^$', 'index'),
    url(r'^parole/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<author_slug>[-\w]+)/(?P<title_slug>[-\w]+)$', 'parole'),
    url(r'^parole/random$', 'random'),
)

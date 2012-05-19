from django.conf.urls import patterns, url

urlpatterns = patterns('parole2.admin.views',
    url(r'^logout', 'logout'),
    url(r'^$', 'index')
)

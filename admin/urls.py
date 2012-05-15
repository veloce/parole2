from django.conf.urls import patterns, include, url

urlpatterns = patterns('admin.views',
    url(r'^$', 'index')

)

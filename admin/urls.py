from django.conf.urls import patterns, url

urlpatterns = patterns('admin.views',
    url(r'^logout', 'logout'),
    url(r'^$', 'index'),
    url(r'^add$', 'add'),
    url(r'^edit/(\d+)', 'edit'),
    url(r'^delete/(\d+)', 'delete'),
)

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^logout', 'parole2.admin.views.logout'),

    url(r'^admin/', include('parole2.admin.urls')),

)

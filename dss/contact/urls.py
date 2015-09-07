from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^view_contact$','contact.views.contact'),
                       url(r'^save_contact$','contact.views.save_contact')
                       )

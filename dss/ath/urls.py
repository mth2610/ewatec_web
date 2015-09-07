from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^login$','ath.views.login'),
                       url(r'^auth_view$','ath.views.auth_view'),
                       url(r'^loggedin$','ath.views.loggedin'),
                       url(r'^invalid_login$','ath.views.invalid_login'),
                       url(r'^logout$','ath.views.logout'),
                       url(r'^signup$','ath.views.signup'),
                       url(r'^register_success$','ath.views.register_success'),
                       url(r'^require_login$','ath.views.require_login'),
                       url(r'^permission_error$','ath.views.permission_error'),
                       url(r'^profile$','ath.views.profile')
                       )
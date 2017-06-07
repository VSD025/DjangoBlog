from django.conf.urls import url
from . import views 


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^search_form/$', views.search_form, name = 'search_form'),
	url(r'^search/$', views.search, name = 'search_result'),
	url(r'^register/$', views.RegisterFormView.as_view(), name = 'registration'),
	url(r'^login/$', views.LoginFormView.as_view(), name = 'login'),
	url(r'^logout/$', views.LogoutView.as_view(), name = 'logout'),

] 
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.nazwa_metody_renderujacej_dany_widok, name='post_list'),
	url(r'^post/(?P<pobrany_parametr>[0-9]+)/$', views.renderuj_widok_z_parametrem, name='nazwa_urla'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
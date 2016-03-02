from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.nazwa_metody_renderujacej_dany_widok, name='post_list'),
	url(r'^post/(?P<pobrany_parametr>[0-9]+)/$', views.renderuj_widok_z_parametrem, name='nazwa_urla'),
]
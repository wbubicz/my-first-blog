from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.nazwa_metody_renderujacej_dany_widok, name='post_list'),
]
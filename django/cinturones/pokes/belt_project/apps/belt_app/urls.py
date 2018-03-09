from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register', views.registration),
    url(r'^dashboard$', views.dashboard),
    url(r'^signout$', views.signout),
    url(r'^users/(?P<id>\d+)$', views.show_user),
    url(r'^add_poke$', views.add_poke)
]

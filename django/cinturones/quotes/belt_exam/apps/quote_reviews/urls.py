from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.registration),
    url(r'^dashboard$', views.dashboard),
    url(r'^signout$', views.signout),
    url(r'^add_fave$', views.add_fave),
    url(r'^remove_fave$', views.remove_fave),
    url(r'^add_quote$', views.add_quote),
    url(r'^users/(?P<id>\d+)$', views.show_user),

]

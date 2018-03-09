from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.registration),
    url(r'^dashboard$', views.dashboard),
    url(r'^signout$', views.signout),
    url(r'^books/add_book_review$', views.add_book_review),
    url(r'^books/add$', views.add),
    url(r'^books/(?P<id>\d+)$', views.show_book_review),
    url(r'^users/(?P<id>\d+)$', views.show_user),
    url(r'^delete/(?P<id>\d+)$', views.delete_review),
]

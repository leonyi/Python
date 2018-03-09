from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^add_course$', views.add_course),
    url(r'^courses/(?P<id>\d+)/remove$', views.render_remove_page),
    url(r'^courses/(?P<id>\d+)/delete$', views.delete_course),
    url(r'^courses/show_comments/(?P<id>\d+)$', views.render_course_comments)
]

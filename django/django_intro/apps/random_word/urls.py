from django.conf.urls import url
from . import views 

print "I am in random_word urls.py"

urlpatterns = [
    url(r'^$', views.index)
]

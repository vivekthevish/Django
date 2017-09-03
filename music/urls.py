from django.conf.urls import url
from . import views
urlpatterns = [
    #Main Page for Music
    url(r'^$', views.index, name='index'),

    #Main page for music details
    url(r'^(?P<album_id>[0-9]+)/$',views.details, name='details')
]
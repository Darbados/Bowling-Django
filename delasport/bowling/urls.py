from django.conf.urls import url
from . import views

app_name = 'bowling'
urlpatterns = [
    url(r'^$', views.NameView.as_view(), name='index'),
    url(r'^add_roll/(?P<game_id>[0-9]+)/$', views.Add_Roll.as_view(), name='add_roll'),
    url(r'^total_score/(?P<game_id>[0-9]+)/$', views.total_score, name='total_score'),
    url(r'^api/(?P<pk>[0-9]+)/$', views.BowlingAPI.as_view()),
]

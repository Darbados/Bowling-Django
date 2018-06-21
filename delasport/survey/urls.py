from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([\w-]+)/$', views.survey, name='survey'),
]
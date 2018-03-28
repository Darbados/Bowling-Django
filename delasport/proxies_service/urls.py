from django.conf.urls import url
import views

app_name = 'proxies_service'

urlpatterns = [
    url(r'^$', views.test, name='index'),
    url(r'^getProxies/$', views.getProxies, name='proxies'),
    url(r'^getParsers/$', views.getParsers, name='parsers')
]
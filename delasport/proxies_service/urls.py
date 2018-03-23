from django.conf.urls import url
import views

app_name = 'proxies_service'

urlpatterns = [
    url(r'^$', views.test, name='index'),
]
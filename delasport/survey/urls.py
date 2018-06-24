from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^form/$', views.form_view, name='form_view'),
    url(r'^completed/$', views.completed, name='completed'),
    url(r'^all/$', views.all_surveys, name='all_surveys')
]
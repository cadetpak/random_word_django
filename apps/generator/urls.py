from django.conf.urls import patterns, url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^generate/', views.generate, name='generate'),
	url(r'^destroy/', views.destroy, name='destroy'),
]
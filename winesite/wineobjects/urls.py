from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'contact', views.contact, name='contact'),
    url(r'still_wine', views.still_wine, name='still_wine'),

]
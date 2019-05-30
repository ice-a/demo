from django.conf.urls import url
from . import views
app_name = 'demo1'
urlpatterns = [
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^wedding/$',views.wedding,name='wedding'),
    url(r'^services/$',views.services,name='services'),
    url(r'^about/$',views.about,name='about'),
    url(r'^index/$',views.index,name='index'),
]

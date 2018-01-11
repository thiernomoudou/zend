from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.save_delivery_order, name='delivery-order'),
    
]
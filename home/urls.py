from . import views
from django.conf.urls import url, include

urlpatterns = [
    
    url('', views.home, name='home'),
    url('about', views.about, name='about'),
    url('cars', views.cars, name='cars'),
    url('contact', views.contact, name='contact'),
    url('service', views.service, name='service'),
    url('gallery', views.gallery, name='gallery'),
    url('elements', views.elements, name='element'),
    url('blog2', views.blog2, name='blog2'),
    url('booking',views.booking, name='booking'),
    url('login',views.login, name='login'),

    url('blog1', views.blog1, name='blog1'),
    url('addcar', views.addcar, name='addcar'),
    url('editcar/<int:carid>', views.addcar, name='addcar'),
    url('updatecar', views.updatecar, name='updatecar'),
    url('delete/<int:carid>', views.deletecar, name='deletecar'),

    ]
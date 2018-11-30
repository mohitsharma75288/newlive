from . import views
from django.conf.urls import url, include

urlpatterns = [
   
    url('', views.dashboard, name='dashboard'),
    url('maps', views.maps, name='maps'),
    url('carlist', views.carlist, name='carlist'),
    url('highchart', views.charts, name='charts'),

    url('booked', views.booked, name='booked'),
    url('booking',views.booking, name='booking'),
    url('signup', views.signup, name='signup'),
    url('typography', views.typography, name='typography'),
    url('table', views.table, name='table'),
    url('notifications', views.notifications, name='notifications'),
    url('user', views.user, name='user'),
    url('upgrade', views.upgrade, name='upgrade'),
    url('addcar', views.addcar, name='addcar'),
    url('editcar/<int:carid>', views.addcar, name='addcar'),
    url('updatecar', views.updatecar, name='updatecar'),
    url('deletecar/<int:carid>', views.deletecar, name='deletecar'),

]
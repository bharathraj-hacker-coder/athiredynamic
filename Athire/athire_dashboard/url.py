from os import name
from django.urls import path

from . import views
urlpatterns = [
    path('', views.signin, name='signin'),
    path('dress_add/', views.dress_add, name='dress_add'),
    path('dress_edit/', views.dress_edit, name='dress_edit'),
    path('dress_delete/', views.dress_delete, name='dress_delete'),
    path('client_add/', views.client_add, name='client_add'),
    path('client_edit/', views.client_edit, name='client_edit'),
    path('client_delete/', views.client_delete, name='client_delete'),
    path('search_dress/', views.search_dress, name='search_dress'),
    path('availability/', views.availability, name='availability'),
    path('booking_details/', views.booking_details, name='booking_details'),
    path('monthly_report/', views.monthly_report, name='monthly_report'),
    path('statistics/', views.statistics, name='statistics'),
    path('non_booked_dress/', views.non_booked_dress, name='non_booked_dress'),
    path('remainder/', views.remainder, name='remainder'),
    path('active_order/', views.active_order, name='active_order'),
]
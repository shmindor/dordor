from django.contrib import admin
from django.urls import path
from . import views
from .views import contact_view, message_list_view
urlpatterns = [
    path('home',views.home, name='home' ),
    path('contact/', contact_view, name='contact'),
    path('messages/', message_list_view, name='message_list'),
    path('success/', views.success_page, name='success_page'),
    path('service/', views.servicePage, name='service'),
]




 

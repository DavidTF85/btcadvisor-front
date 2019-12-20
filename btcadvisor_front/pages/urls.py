"""
pages/urls.py
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

#front-end URLs
urlpatterns = [

    # Homepage URLs
    path('', views.welcome_page, name='welcome_page'),
    path('contactus', views.contactus_page, name='contactus_page'),

    # Gateway URLs
    path('register', views.register_page, name='register_page'),
    path('register/success', views.register_success_page, name='register_success_page'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_page, name='logout_page'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

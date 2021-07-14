from django.urls import path
from . import views
urlpatterns = [
    path('', views.log_and_reg),
    path('register', views.register),
    path('success', views.success),
    path('logout', views.logout),
    path('login', views.login),
]
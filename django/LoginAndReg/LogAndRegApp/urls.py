from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    # path('wall', views.wall),
    # path('post_message', views.create_message),
    # path('post_comment', views.post_comment),

]
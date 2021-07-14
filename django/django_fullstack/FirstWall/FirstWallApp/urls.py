from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('post_message', views.post_message),
    path('add_comment/<int:id>', views.post_comment),
    path('delete_comment/<int:id>', views.delete_comment),
    path('delete_message/<int:id>', views.delete_message),

]
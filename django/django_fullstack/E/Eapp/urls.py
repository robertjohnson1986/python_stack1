from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('post_title', views.post_title),
    # path('post description', views.post_description),
    path('like_message/<int:id>', views.like),
    
    path('unlike_message/<int:id>', views.unlike),
    # path('delete_comment/<int:id>', views.delete_comment),
    path('delete_message/<int:id>', views.delete_message),
    path('book_page/<int:id>', views.book_page),
    path('update/<int:id>', views.update),
    # path('grant_wish/<int:id>', views.grant_wish)

]
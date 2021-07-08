from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/shows
    path('', views.index),
    # localhost:8000/shows/new
    path('new', views.new),
    path('create', views.create),
    # localhost:8000/shows/<show_id>
    path('<int:show_id>', views.show),
    path('<int:show_id>/edit', views.edit),
    path('<int:show_id>/update', views.update),
    path('<int:show_id>/delete', views.delete),
]
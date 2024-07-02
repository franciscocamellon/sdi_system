from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tourist/", views.tourist, name="tourist"),
    path("journalist/", views.journalist, name="journalist"),
    path("citizen_scientist/", views.citizen_scientist, name="citizen_scientist"),
    path("gi_specialist/", views.gi_specialist, name="gi_specialist"),
]

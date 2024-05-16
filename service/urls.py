from django.urls import path
from . import views

urlpatterns = [
    path("",  view=views.services_list_view, name="services_list"),
    path("<str:title>/",  view=views.services_detail_view, name="services_detail"),
]
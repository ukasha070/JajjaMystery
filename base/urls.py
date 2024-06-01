from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("about/", views.about_view, name="about_view"),
    path("logout/", views.logout_view, name="logout_view"),
    path("contact/", views.contact_view, name="contact_view"),
    path("testimonials/", views.testimonials_view, name="testimonials_view"),
    path("send-message/",  view=views.send_contact_message_view, name="send_contact_message"),
]
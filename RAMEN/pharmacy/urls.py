from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("index/",views.dome_form, name="index"),
    path("about/",views.about_dr_kali, name="about"),
    path("",auth_views.LoginView.as_view(template_name = "products/login.html"), name="login"),
]

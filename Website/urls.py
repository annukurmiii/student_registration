from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("contactus/", views.contactus, name="contactus"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("payment/", views.payment, name="payment"),
]
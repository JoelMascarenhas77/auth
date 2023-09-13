from django.urls import path
from . import views


urlpatterns = [
    path("", views.home ),
    path("login/", views.userlogin ),
    path("signup/", views.usersignup ),
    path("dash/", views.dash),
    path("logout/", views.out),
    
]

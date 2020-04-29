from . import views
from django.urls import path

urlpatterns = [

    path('home/',views.home),
    path('user/',views.UserView.as_view()),
    path("register/", views.register, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
]

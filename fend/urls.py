from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("signout", views.logout, name="logout"),
    path("regdetail", views.regdetail, name="regdetail"),
    path("runsearch", views.runsearch, name="runsearch"),
    #path("output", views.output, name="output"),
]
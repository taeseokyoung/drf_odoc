from django.urls import path, include
from users import views


urlpatterns = [
    path("", views.UserView.as_view()),
    path("login/", views.UserLoginView.as_view()),

]

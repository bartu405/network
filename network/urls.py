
from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("like", views.like, name="like"),
    path("edit", views.edit, name="edit"),
    path("register", views.register, name="register"),
    path("newPost", views.newPost, name="newPost"),
    path("following", views.following  , name="following"),
    path("<str:profile>", views.profile, name="profile"),
    path("follow/<str:profile>", views.follow, name="follow"),
    path("unfollow/<str:profile>", views.unfollow, name="unfollow")
    
]

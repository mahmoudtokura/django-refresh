from django.urls import path

from . import views

app_name = "blogapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search_blog, name="search_blog"),
    path("my-blogs/", views.user_blogs, name="user_blogs"),
    path("create/", views.create_blog, name="create_blog"),
    path("<str:slug>/", views.details, name="details"),
    path("<str:slug>/update", views.update_blog, name="update_blog"),
    path("<str:slug>/delete", views.delete_blog, name="delete_blog"),
]

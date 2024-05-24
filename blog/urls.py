from django.urls import path

from blog import views

urlpatterns = [
    path("", views.index, name="index_blog"),
    path("posts", views.posts),
    path("post/<slug:slug>", views.post_detail),
]

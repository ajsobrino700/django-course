from django.urls import path

from . import views

urlspattern = [
    path("", views.index, name="index"),
    path("posts",views.posts),
    path("posts/<slug:slug>",views.post_detail),
]

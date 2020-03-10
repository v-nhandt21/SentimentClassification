from django.urls import path
from Machine import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("paper/", views.paper, name="paper"),
    path("demo/", views.demo, name="demo"),
    path("thachthuc/", views.thachthuc, name="thachthuc"),
]
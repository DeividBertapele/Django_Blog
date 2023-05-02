from django.urls import path

from .views import frontpage, about, robots_txt

urlpatterns = [
    path("robots.txt", robots_txt, name="robots_txt"),
    path("", frontpage, name="frontpage"),
    path("about/", about, name="about"),
]
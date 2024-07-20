from django.urls import path
from my_django_blog.article import views

urlpatterns = [
    path('', views.index),
]
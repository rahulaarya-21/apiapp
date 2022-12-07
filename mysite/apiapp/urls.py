from django.urls import path
from apiapp.views import *
urlpatterns = [
    path('article/', article_list),
    path("details/<int:pk>/",article_details)
]
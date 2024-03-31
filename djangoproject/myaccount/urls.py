from django.urls import path

from . import views
from .views import RegisterAPIView,LoginAPI
from knox.views import LogoutView,LogoutAllView

urlpatterns=[
    path('register/',RegisterAPIView.as_view(),name='register'),
    path('login/',LoginAPI.as_view()),
    path('logout/',LogoutView.as_view()),
    path('logout-all/',LogoutAllView.as_view()),
]
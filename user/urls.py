from django.urls import path
from . import views

urlpatterns=[
    path('',views.UserloginView.as_view()),
    path('register', views.UserRegister.as_view())
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.login, name='login'),
    path('index', views.index, name='index'),
    path("upload_excel/", views.upload_excel, name="upload_excel"),
    path("uploaded_excel/", views.uploaded_excel, name="uploaded_excel"),
    path("logout/", views.logout, name="logout")
]    
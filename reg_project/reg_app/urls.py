from django.contrib import admin
from django.urls import path
from reg_app import views

app_name = "reg_app"

urlpatterns = [
    path('', views.index, name="index"),
    path('entry/', views.EnteryListView, name="EnteryListView")
]

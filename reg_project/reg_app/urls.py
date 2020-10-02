from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as ath_v

app_name = "reg_app"

urlpatterns = [
    path('index', views.index, name="home"),
    url(r'^entry$', views.entry, name="entry"),
    #path('login/', views.Login, name="Login"),
    path('Entry_detail/<int:entry_id>', views.Entry_detail, name="Entry_detail"),
    path('sent/', views.Sent, name="Sent"),
    url("Login", ath_v.LoginView.as_view(), name="Login"),
    url("Logout", ath_v.LogoutView.as_view(), name="Logout"),

    # update,edit,delete entry urls
    path('', views.Parent, name="parent"),
    url(r'^create$', views.create_entry, name='create'),
    url(r'^edit_entry/(?P<entry_id>\d+)$', views.edit_entry, name='edit_entry'),
    url(r'^edit_entry/update/(?P<entry_id>\d+)$',
        views.update_entry, name='update'),
    url(r'^delete_entry/(?P<entry_id>\d+)$',
        views.delete_entry, name="delete_entry"),



    path('add_entry', views.add_entry, name='add_entry'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

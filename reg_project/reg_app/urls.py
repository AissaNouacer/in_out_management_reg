from django.contrib import admin
from django.urls import path
from reg_app import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as ath_v

app_name = "reg_app"

urlpatterns = [
    path('', views.index, name="home"),
    path('entry/', views.EnteryListView, name="EnteryListView"),
    #path('login/', views.Login, name="Login"),
    path('Entry_detail/<int:entry_id>', views.Entry_detail, name="Entry_detail"),
    path('sent/', views.Sent, name="Sent"),
    url("Login", ath_v.LoginView.as_view(), name="Login"),
    url("Logout", ath_v.LogoutView.as_view(), name="Logout"),
    # update,edit,delete entry urls
    path('add_entry', views.add_entry, name='add_entry'),
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
    path('update_entry/<int:entry_id>', views.update_entry, name='update_entry'),
    path('delete_entry/<int:entry_id>', views.delete_entry, name="delete_entry"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

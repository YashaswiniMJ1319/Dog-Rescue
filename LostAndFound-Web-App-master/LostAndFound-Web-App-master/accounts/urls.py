from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('request/', views.requestItem, name='request_item'),
    path('profile/edit', views.editprofile, name='edit_profile'),
    path('password/', views.change_password, name='change_password'),
    re_path(r'^claim/(?P<id>\d+)/$', views.claim, name='claim'),
]

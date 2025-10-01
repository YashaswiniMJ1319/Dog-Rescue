from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Home page and Dog-related pages
    path('', views.home, name='home'),
    path('dogs/name/', views.dogs_by_name, name='dogs_by_name'),
    path('dogs/breed/', views.dogs_by_breed, name='dogs_by_breed'),
    path('dogs/available/', views.available_dogs, name='available_dogs'),
    path('dogs/recent/', views.recent_dogs, name='recent_dogs'),
    
    # User registration and authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('add-dog/', views.add_dog, name='add_dog'),
    path('dogs/status/<str:status>/', views.dogs_by_status, name='dogs_by_status'),
    path('dogs/filter/', views.filter_dogs, name='filter_dogs'),
     
    
    path('missing/', views.missing_dogs, name='missing_dogs'),
     
    path('contact/', views.contact, name='contact'),

]

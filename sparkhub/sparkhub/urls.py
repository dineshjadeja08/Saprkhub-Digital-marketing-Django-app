from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include all URLs from app.urls, no need to add '/app/' prefix unless necessary
    path('accounts/', include('allauth.urls')),  # for authentication views like sign in, sign up
    path('', views.home, name='home'),  # Home page path
    path('app/', include('app.urls')),  # Make sure this is for app-specific routes
    path('dashboard/', views.dashboard, name='dashboard'),
]

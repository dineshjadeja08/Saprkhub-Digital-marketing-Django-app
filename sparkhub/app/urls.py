from django.urls import path, include
from . import views

urlpatterns = [
    path('influencers/', views.influencer_list, name='influencer_list'),
    path('brands/', views.brand_list, name='brand_list'),
    path('campaigns/', views.campaign_list, name='campaign_list'),
    path('accounts/', include('allauth.urls')),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='signout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('discover-influencers/', views.discover_influencers, name='discover_influencers'),
    path('create-campaign/', views.create_campaign, name='create_campaign'),
    path('generate-report/', views.generate_report, name='generate_report'),
]

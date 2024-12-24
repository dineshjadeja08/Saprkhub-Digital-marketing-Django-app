from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import Influencer, Brand, Campaign
from .forms import CampaignForm

def home(request):
    return render(request, 'home.html')

# Sign-Up View
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully! Welcome, {username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})

# Sign-In View
def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/signin.html', {'form': form})

def signout(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect('signin')

@login_required
def dashboard(request):
    # Action cards with progress data
    action_cards = [
        {
            'title': 'Find Relevant Influencers',
            'description': 'Discover the power of finding "Relevant Influencers" with our platform...',
            'button_text': 'Discover Influencers',
            'link': 'discover_influencers',
            'progress': 60,  # Example progress (in %)
        },
        {
            'title': 'Promote Your Brand',
            'description': 'Elevate your brand\'s presence and reach with our expert promotional services...',
            'button_text': 'Create Campaign',
            'link': 'create_campaign',
            'progress': 80,
        },
        {
            'title': 'Track & Analyze Campaigns',
            'description': 'Gain valuable insights and measure the success of your campaigns...',
            'button_text': 'Generate Report',
            'link': 'generate_report',
            'progress': 40,
        },
    ]

    # Mock recent activities with timestamps
    recent_activities = [
        {'activity': 'You created a new campaign', 'timestamp': '2024-12-18 14:32'},
        {'activity': 'You connected with 3 new influencers', 'timestamp': '2024-12-17 10:15'},
        {'activity': 'Your campaign report is ready for download', 'timestamp': '2024-12-16 09:50'},
    ]

    # Mock notifications
    notifications = [
        {'message': '2 new influencers matched your criteria!', 'type': 'info'},
        {'message': 'Your subscription will expire in 5 days.', 'type': 'warning'},
        {'message': 'Your report is ready for download.', 'type': 'success'},
    ]

    return render(request, 'dashboard/home.html', {
        'action_cards': action_cards,
        'recent_activities': recent_activities,
        'notifications': notifications,
    })

def discover_influencers(request):
    influencers = Influencer.objects.all()
    return render(request, 'dashboard/discover_influencers.html', {
        'title': 'Discover Influencers',
        'influencers': influencers,
    })

def create_campaign(request):
    if request.method == 'POST':  # If the form is submitted
        form = CampaignForm(request.POST)
        if form.is_valid():  # Check if the data is valid
            form.save()  # Save the form data to the database
            messages.success(request, 'Campaign created successfully!')
            return redirect('dashboard')  # Redirect to the dashboard
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CampaignForm()  # Display an empty form if the page is visited without submission

    return render(request, 'create_campaign.html', {'form': form})

def generate_report(request):
    campaigns = Campaign.objects.all()
    return render(request, 'dashboard/generate_report.html', {
        'title': 'Generate Report',
        'campaigns': campaigns,
    })

def influencer_list(request):
    influencers = Influencer.objects.all()
    return render(request, 'influencers/list.html', {'influencers': influencers})

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'brands/list.html', {'brands': brands})

def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, 'campaigns/list.html', {'campaigns': campaigns})
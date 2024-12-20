from django import forms
from .models import Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign  # Link this form to the Campaign model
        fields = ['name', 'description', 'target_audience', 'budget', 'start_date', 'end_date']  # Fields to include in the form

        # Customizing form fields for better user experience
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter campaign name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'target_audience': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter target audience'}),
            'budget': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter budget'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

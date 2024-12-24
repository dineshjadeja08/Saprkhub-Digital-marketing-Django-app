from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Influencer(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='influencers/', blank=True, null=True)
    social_links = models.JSONField(help_text="Store links in JSON format: {'platform': 'url'}", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='brands/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Campaign(models.Model):
    name = models.CharField(max_length=255, default="Default Campaign Name")
    description = models.TextField(default="No description provided")
    target_audience = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    status = models.CharField(
        max_length=50,
        choices=[
            ('ongoing', 'Ongoing'),
            ('completed', 'Completed'),
            ('upcoming', 'Upcoming'),
        ],
        default='upcoming',
    )
    influencer = models.ForeignKey(
        Influencer,
        on_delete=models.CASCADE,
        related_name='campaigns',
        help_text="Select the influencer associated with this campaign."
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='campaigns',
        help_text="Select the brand associated with this campaign."
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.influencer.name} x {self.brand.name}"

from django.db import models
from django.utils import timezone
timezone.now
from datetime import datetime

class Influencer(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='influencers/')
    social_links = models.JSONField()

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='brands/')
    website = models.URLField()

    def __str__(self):
        return self.name

class Campaign(models.Model):
    name = models.CharField(max_length=255, default="Default Campaign Name")
    description = models.TextField(default="No description provided")
    target_audience = models.CharField(max_length=255)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField(default=datetime.now)

    # Add foreign keys to Influencer and Brand
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.influencer.name} x {self.brand.name}"

    

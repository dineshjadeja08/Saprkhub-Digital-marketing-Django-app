from django.contrib import admin
from .models import Influencer, Brand, Campaign

# Registering the models with the admin site
admin.site.register(Influencer)
admin.site.register(Brand)
admin.site.register(Campaign)

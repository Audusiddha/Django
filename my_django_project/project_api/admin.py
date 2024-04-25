from django.contrib import admin
from project_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
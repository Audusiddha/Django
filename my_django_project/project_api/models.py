from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings 
# Define a custom manager for the user profile model
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    # Method to create a standard user
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        # Normalize the email address (convert to lowercase)
        email = self.normalize_email(email)
        # Create a new user instance
        user = self.model(email=email, name=name)

        # Set the password for the user
        user.set_password(password)
        # Save the user to the database
        user.save(using=self._db)

        return user

    # Method to create a superuser
    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        # Create a standard user using the create_user method
        user = self.create_user(email, name, password)

        # Assign superuser and staff status to the user
        user.is_superuser = True
        user.is_staff = True
        # Save the user with superuser status
        user.save(using=self._db)

        return user

# Define the user profile model
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    # Define fields for the user profile model
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Define the custom manager for the user profile model
    objects = UserProfileManager()

    # Set the email field as the unique identifier for authentication
    USERNAME_FIELD = 'email'

    # Specify additional fields required when creating a user (excluding password and email)
    REQUIRED_FIELDS = ['name']

    # Method to get the full name of the user
    def get_full_name(self):
        """Retrieve full name for user"""
        return self.name

    # Method to get the short name of the user
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    # Method to return a string representation of the user
    def __str__(self):
        """Return string representation of user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile  = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE

    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text
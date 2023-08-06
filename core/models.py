from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(User):
    profile_image = models.ImageField(upload_to="users/profiles")
    date_of_birth = models.DateField(null=True)
    bio = models.TextField(null=True)

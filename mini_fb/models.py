# mini_fb/models.py
from django.db import models


# Create your models here.
class Profile(models.Model):
    """
    Model file to represent Facebook user profile data.
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    email = models.EmailField()
    image_url = models.URLField()

    def __str__(self):
        """
        Return the string representation of each Fb profile,
        which is the user first and last name
        """
        return f"{self.first_name} {self.last_name}"

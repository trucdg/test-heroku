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

    def get_status_messages(self):
        """
        return a queryset of StatusMessage for which the profile is this Profile,
        and is ordered by timestamp
        """
        status_messages = StatusMessage.objects.filter(profile=self).order_by(
            "-timestamp"
        )

        return status_messages


class StatusMessage(models.Model):
    """
    Model to represent Facebook status messages for a profile
    """

    timestamp = models.DateTimeField(auto_now=True)
    message = models.TextField()
    # foreign key references a Profile
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return the string representation for the status message
        """
        return self.message

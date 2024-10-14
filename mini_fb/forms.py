from django import forms
from .models import Profile, StatusMessage


class CreateProfileForm(forms.ModelForm):
    """
    A form class to create and update Profile instances
    This form fields correspond to the Profile model attributes
    """

    class Meta:
        """
        This metadata class defines the model to use and the fields that will be included in the form
        """

        # Specify the model that this form associated with
        model = Profile
        fields = ["first_name", "last_name", "city", "email", "image_url"]


class CreateStatusMessageForm(forms.ModelForm):
    """
    A form class to create a StatusMessage instance that is associated with a Profile
    """

    class Meta:
        """
        This meta class defines the model to use and the fields that will be included in the form
        """

        model = StatusMessage
        fields = ["message"]

from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile


# Create your views here.
class ShowAllProfilesView(ListView):
    """
    A view class to display all profiles stored in the Profile model
    """

    # Specify the model to be listed in the view
    model = Profile

    # the template that will be used to display the profile data
    template_name = "mini_fb/show_all_profiles.html"

    # the name of the object manager that store all profiles
    context_object_name = "profiles"

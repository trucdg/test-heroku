from typing import Any
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile, StatusMessage
from .forms import CreateProfileForm, CreateStatusMessageForm
from django.urls import reverse


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


class ShowProfilePageView(DetailView):
    """
    A view class to display a single profile page
    """

    model = Profile

    template_name = "mini_fb/show_profile.html"

    context_object_name = "profile"


class CreateProfileView(CreateView):
    """
    a class inherits from the generic CreateView class
    handles request to URL: '/mini_fb/create_profile/'
    - on GET: returns a form to create a Profile instance
    - on POST: process and validate the form,
               then create and save the new Profile,
               then redirect to the DetailView of this Profile

    """

    # Specify the form that this view use
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"

    def form_valid(self, form):
        """
        This method is called after the form is validated
        before saving the data to the database
        """
        print(f"CreateProfileView.form_valid(): form={form.cleaned_data}")
        print(f"CreateProfileView.form_valid(): self.kwargs={self.kwargs}")
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        this method is called when the form is invalid
        """
        print(f"CreateProfileView.form_invalid(): form={form.cleaned_data}")
        print(f"CreateProfileView.form_invalid(): self.kwargs={self.kwargs}")
        return super().form_invalid(form)

    def get_success_url(self) -> str:
        """
        return the URL to redirect on success
        """
        return reverse("mini_fb:show_profile", kwargs={"pk": self.object.pk})


class CreateStatusMessageView(CreateView):
    """
    A class inherits from the CreateView django generic view
    handles request to URL /mini_fb/profile/<int:pk>/create_status
    on GET: return a form to create a StatusMessage instance
    on POST: validate the form, save data and redirect to the Profile detail view
    """

    form_class = CreateStatusMessageForm
    template_name = "mini_fb/create_status_form.html"

    def form_valid(self, form):
        """
        this method is called when the form is valid, and before saving data to database
        """
        print(f"CreateStatusMessageView.form_valid(): form={form.cleaned_data}")
        print(f"CreateStatusMessageView.form_valid(): self.kwargs={self.kwargs}")

        # find the Profile specified by the kwargs obtained by the URL
        profile = Profile.objects.get(pk=self.kwargs["pk"])

        # Attach the StatusMessage instance created by the form to the profile
        form.instance.profile = profile

        return super().form_valid(form)

    def form_invalid(self, form):
        """
        this method is called when the form is invalid
        used for debugging purpose
        """
        print(f"CreateStatusMessageView.form_invalid(): form={form.cleaned_data}")
        print(f"CreateStatusMessageView.form_invalid(): self.kwargs={self.kwargs}")
        return super().form_invalid(form)

    def get_success_url(self):
        """
        return the URL on success
        """
        # find the Profile associated with the pk specified by the kwargs obtained by the URL
        # profile = Profile.objects.get(self.kwargs['pk'])
        return reverse("mini_fb:show_profile", kwargs=self.kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """
        provide extra context data to the template
        """

        # first, get all the context data from the super class
        context = super().get_context_data(**kwargs)

        # find the Profile identifies by the PK specified by the URL pattern
        profile = Profile.objects.get(pk=self.kwargs["pk"])

        # add the Profile into the context
        context["profile"] = profile

        # return the context to be used by the template
        return context

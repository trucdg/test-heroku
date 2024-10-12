from django.urls import path
from . import views

app_name = "mini_fb"

urlpatterns = [
    path(r"", views.ShowAllProfilesView.as_view(), name="show_all_profiles_view"),
    path(r"profile/<int:pk>", views.ShowProfilePageView.as_view(), name="show_profile"),
]

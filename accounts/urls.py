from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
from .views import signup_view, profile_view, edit_profile

urlpatterns = [
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("signup/", signup_view, name="signup"),
    path("profile/", profile_view, name="profile"),
    path("profile/edit/", edit_profile, name="edit_profile"),

    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'), name='password_change_done'),
]

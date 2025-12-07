from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile

urlpatterns = [
    # Login (uses Django's LoginView)
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),

    # Logout (uses Django's LogoutView)
    path("logout/", auth_views.LogoutView.as_view(template_name="registration/logged_out.html"), name="logout"),

    # Registration
    path("register/", register, name="register"),

    # Profile (view/edit)
    path("profile/", profile, name="profile"),
]

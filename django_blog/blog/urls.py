from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    # Login (uses Django's LoginView)
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),

    # Logout (uses Django's LogoutView)
    path("logout/", auth_views.LogoutView.as_view(template_name="registration/logged_out.html"), name="logout"),

    # Registration
    path("register/", register, name="register"),

    # Profile (view/edit)
    path("profile/", profile, name="profile"),

    path('posts/', PostListView.as_view(), name='post-list'),                  # list
    path('posts/new/', PostCreateView.as_view(), name='post-create'),         # create
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),    # detail
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),# edit
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),# delete
]

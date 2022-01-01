from .views import RegisterView, LoginView, UserProfileView
from django.urls import path


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('profile', UserProfileView.as_view(), name='profile'),
]
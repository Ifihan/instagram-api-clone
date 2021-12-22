from .views import RegisterView, LoginView, AuthUserDataView
from django.urls import path


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('profile', AuthUserDataView.as_view(), name='profile'),
]
from django.urls import path
from posts.views import PostView

urlpatterns = [
    path('', PostView.as_view(), name='posts'),
]
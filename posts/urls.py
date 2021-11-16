from django.urls import path
from posts.views import CreatePostView, ReadPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', CreatePostView.as_view(), name='post'),
    path('<int:pk>/', ReadPostView.as_view(), name='read-post'),
    path('update/<int:pk>/', UpdatePostView.as_view(), name='update-post'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name='delete-post'),
]
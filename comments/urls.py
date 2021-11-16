from django.urls import path
from comments.views import CommentsView

urlpatterns = [
    path('', CommentsView.as_view(), name='comments'),
]
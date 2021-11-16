from django.urls import path
from comments.views import CreateCommentView, ListCommentView, UpdateCommentView, DeleteCommentView

urlpatterns = [
    path('', CreateCommentView.as_view(), name='comments'),
    path('<int:pk>', ListCommentView.as_view(), name='list-comments'),
    path('update/<int:pk>/', UpdateCommentView.as_view(), name='update-comment'),
    path('delete/<int:pk>/', DeleteCommentView.as_view(), name='delete-comment')
]
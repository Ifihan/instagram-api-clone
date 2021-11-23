from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser

from posts.models import Posts
from posts.serializers import PostsSerializer
# Create your views here.
class CreatePostView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = [MultiPartParser]
    def post(self, request, format=None):
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReadPostView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request, pk, format=None):
        try:
            post = Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostsSerializer(post)
        return Response(serializer.data)

class UpdatePostView(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostsSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeletePostView(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class BookmarkPost

# liked posts feed view
# bookamrk posts
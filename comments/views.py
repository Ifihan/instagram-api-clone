from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from comments.models import Comments
from comments.serializers import CommentsSerializer
# Create your views here.

class CreateCommentView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListCommentView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request):
        comments = Comments.objects.all()
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

class UpdateCommentView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        comment = Comments.objects.get(pk=pk)
        serializer = CommentsSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteCommentView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        comment = Comments.objects.get(pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# liked comments feed view
from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from comments.models import Comments
# from comments.serializers import CommentsSerializer
# Create your views here.

# class CommentView(APIView):
#     def get(self, request, format=None):
#         comments = Comments.objects.all()
#         serializer = CommentsSerializer(comments, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = CommentsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
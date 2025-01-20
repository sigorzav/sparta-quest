from django.shortcuts import render
from django.views.decorators.http import require_POST
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from post.models import Post
from post.serializers import PostSerializers


# 커스텀 APIView
class CustomAPIView(APIView):
    
    def get_object(self, model, pk):
        return model.objects.get(pk=pk)


# 게시판 목록 조회 및 등록
class PostListAPIView(CustomAPIView):
    
    # 게시물 목록 조회
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data)
    
    # 게시물 등록
    def post(self, request):
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 게시물 상세조회/수정/삭제
class PostDetailAPIView(CustomAPIView):
    
    # 게시물 상세조회
    def get(self, request, post_pk):
        post = self.get_object(Post, post_pk)
        serializer = PostSerializers(post)
        return Response(serializer.data)
    
    # 게시물 수정
    def put(self, request, post_pk):
        post = self.get_object(Post, post_pk)
        serializer = PostSerializers(post, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    # 게시물 삭제
    def delete(self, request, post_pk):
        post = self.get_object(Post, post_pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
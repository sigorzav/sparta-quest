from django.shortcuts import render
from django.views.decorators.http import require_POST
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from post.models import Post, Comment
from .serializers import PostSerializers, CommentSerializers


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
    

# 좋아요
class LikesAPIView(CustomAPIView):
    
    def post(self, request, *args, **kwargs):
        post_pk = self.kwargs.get('post_pk')
        post = self.get_object(Post, post_pk)
        
        # 좋아요 취소
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        # 좋아요 추가
        else:
            post.likes.add(request.user)
            liked = True
        
        data = {
            "liked": liked,
            "likes_count": post.get_likes_count
        }
        return Response(data)
    
# 댓글 조회/작성
class CommentListAPIView(CustomAPIView):

    # 댓글 조회
    def get(self, request, *args, **kwargs):
        post_pk = self.kwargs.get('post_pk')
        post = self.get_object(Post, post_pk)
        
        comments = post.comments.all()
        
        serializer = CommentSerializers(comments, many=True)
        return Response(serializer.data)
        
    # 댓글 작성
    def post(self, request, *args, **kwargs):
        post_pk = self.kwargs.get('post_pk')
        post = self.get_object(Post, post_pk)

        serializer = CommentSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 댓글 수정/삭제  
class CommentDetailAPIView(CustomAPIView):

    # 댓글 수정
    def put(self, request, *args, **kwargs):
        comment_pk = self.kwargs.get('comment_pk')
        comment = self.get_object(Comment, comment_pk)
        serializer = CommentSerializers(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
            

    # 댓글 삭제
    def delete(self, request, *args, **kwargs):
        comment_pk = self.kwargs.get('comment_pk')
        comment = self.get_object(Comment, comment_pk)
        comment.delete()
        
        data = {
            "comment_pk": comment_pk,
            "author": comment.author.id,
            "post": comment.post.id,
            "content": comment.content,
        }
        return Response(data)    
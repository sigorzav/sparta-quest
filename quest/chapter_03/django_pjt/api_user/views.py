from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from user.models import User
from .serializers import (
    UserSerializer,
    SignUpSerializer,
    ProflieSerializer
)


class CustomAPIView(APIView):
    
    def get_object(self, model, pk):
        return model.objects.get(pk=pk)


# 회원가입
@api_view(["POST"])
def signup(request):
    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
            

# 사용자 조회
@api_view(["GET"])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# 사용자 상세 조회/수정/삭제
@api_view(["GET"])
def user_detail(request, user_pk):
    user = User.objects.get(pk=user_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)
    

# 프로필 조회/수정
class ProfileAPIView(CustomAPIView):
    
    # 프로필 조회
    def get(self, request, user_pk):
        profile = self.get_object(User, user_pk)
        serializer = ProflieSerializer(profile)
        return Response(serializer.data) 
    
    def put(self, request, user_pk):
        profile = self.get_object(User, user_pk)
        serializer = ProflieSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
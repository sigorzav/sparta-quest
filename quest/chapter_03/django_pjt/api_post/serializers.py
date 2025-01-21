from rest_framework import serializers
from django.utils.dateformat import format
from post.models import Post, Comment

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        
class CommentSerializers(serializers.ModelSerializer):
    # 사용자 or 포맷팅 필드 추가
    # SerializerMethodField :: 읽기 전용 필드
    user_details = serializers.SerializerMethodField()
    formatted_date = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'post', 'user_details', 'formatted_date']
        read_only_fields = ("author", "post",)

    # 직렬화 실행 시점에 메소드를 호출하여, 값을 채워줌
    def get_user_details(self, obj):
        return {
            "nickname": obj.author.nickname,
            "profile_img": obj.author.profile_img.url
        }

    def get_formatted_date(self, obj):
        return {
            'created_at': format(obj.created_at, 'Y-m-d H:i:s'),
            'updated_at': format(obj.updated_at, 'Y-m-d H:i:s')
        }
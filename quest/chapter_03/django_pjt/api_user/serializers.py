from rest_framework import serializers
from user.models import User


# 사용자
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = "__all__"
        

# 회원가입
class SignUpSerializer(serializers.ModelSerializer):
    
    # write_only=True :: 응답에서 제외
    # User Model에는 password만 존재하기 때문에 별도 구현
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ["id", "username", "password", "confirm_password", "nickname", "profile_img", "bio"]
        read_only_fields = ("id",)
        
    # 유효성 체크
    #  - validate_<fieldname> 형식으로 작성
    #  - 수정 또는 검증된 데이터 반드시 return 
    #  - serializers.ValidationError 예외 처리
    #  - attrs 는 dict 이어야 함 (typeError 시 체크)
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Password do not Match")
        return attrs
            
    # create 메소드 정의
    #  - validated_data :: is_valid() 에서 성공한 데이터를 담고 있음
    def create(self, validated_data):
        # User 에서 사용하지 않는 필드 제거
        validated_data.pop('confirm_password', None)
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            nickname=validated_data['nickname'],
            # profile_img=validated_data['profile_img'],
            bio=validated_data['bio'],
        )
        return user
    

# 프로필
class ProflieSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "nickname", "profile_img", "bio"]
from django.db import models

# Timestamp 공통 상속 모델
class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # 생성 시 자동 설정
    updated_at = models.DateTimeField(auto_now=True)      # 수정 시 자동 갱신
    
    class Meta:
        abstract = True  # 데이터베이스 테이블 생성 X

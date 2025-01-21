from django.db import models
from django.conf import settings
from common.models import TimestampModel


# 게시물
class Post(TimestampModel):
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="post")
    title       = models.CharField(max_length=50)
    content     = models.TextField()
    post_img    = models.ImageField(blank=True, upload_to='post_imgs/')
    views       = models.IntegerField(default=0)
    likes       = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likes", blank=True)
    tags        = models.ManyToManyField('Tag', related_name="tags", blank=True)
    
    # 이미지 조회 (기본값 설정)
    @property
    def get_image_url(self):
        if self.post_img:
            return self.post_img.url
        return '/static/common/images/default.jpg'
    
    # 좋아요 건수
    @property
    def get_likes_count(self):
        return self.likes.count()
    
    # 게시물 댓글
    @property
    def get_comments(self):
        return self.comments.select_related('author').all().order_by("created_at")
    

# 댓글
class Comment(TimestampModel):
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    post        = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content     = models.TextField()
    

# 태그   
class Tag(models.Model):
    tag = models.CharField(max_length=20)
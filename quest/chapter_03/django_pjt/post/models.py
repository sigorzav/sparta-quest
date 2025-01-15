from django.db import models
from django.conf import settings
from common.models import TimestampModel

class Post(TimestampModel):
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="post")
    title       = models.CharField(max_length=50)
    content     = models.TextField()
    post_img    = models.ImageField(blank=True, upload_to='post_imgs/')
    views       = models.IntegerField(default=0)
    
    def get_image_url(self):
        if self.post_img:
            return self.post_img.url
        return '/static/common/images/default.jpg'
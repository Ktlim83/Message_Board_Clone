  
from django.db import models
from log_reg_app.models import User


class PostManager(models.Manager):
    def validate(self, form_data):
        errors = {}
        # needs content
        if len(form_data['content']) < 1:
            errors['content'] = 'Content should not be empty.'
            
        return errors

class Post(models.Model):
    content = models.CharField(max_length=255)
    user_likes = models.ManyToManyField(User, related_name='liked_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author_id
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    
    
    def __str__(self):
        return f"{self.id}{self.content}"
    
class Comment(models.Model):
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    message_post = models.ForeignKey(Post, related_name="post_comments", on_delete=models.CASCADE)
    
    

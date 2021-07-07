from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from users.models import Profile
from django.core.validators import FileExtensionValidator


# Create your models here.

class Post(models.Model):
    content = models.TextField( blank = True)
    picture = models.ImageField(upload_to = 'pictures/', blank = True, null = True, validators = [FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    dateposted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'posts')
    liked = models.ManyToManyField(Profile, blank=True, related_name='likes')
    
    
    
    def __str__(self):
        return str(self.content[:20])

    def num_likes(self):
        return self.liked.all().count()

    def num_comment(self):
        return self.comment_set.all().count()

     
   


    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})



    #resizing

    
    # def __str__(self):
    #     return f'{self.user.username}s profile'
    

def save(self, *args, **kwargs):
    super().save(*args, **kwargs)


    img = Image.open(self.picture.path)

    if img.height > 300 or img.width > 300:
        output_size = (300,300) 
        img.thumbnail(output_size)
        img.save(self.picture.path)


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.pk)

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike','Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"
    








#18:00

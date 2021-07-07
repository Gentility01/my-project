from django.db import models
from django.contrib.auth.models  import User
from PIL import Image   
# from blog.models import Post    
from django.db.models.fields import DateField, DateTimeField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    friends = models.ManyToManyField(User, blank=True, related_name='friends')


    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()



    def __str__(self):
        return f"{self.user.username}'s profile"

    def get_posts_no(self):
        return self.posts.all().count()

    def get_all_authors_post(self):
        return self.posts.all()

    def get_likes_given_no(self):
        likes = self.like_set.all()
        total_liked = 0
        for item in likes:
            if item.value=='Like':
                total_liked += 1
        return total_liked


    def get_likes_recieved_no(self):
        posts = self.posts.all()
        total_liked = 0
        for item in posts:
            total_liked += item.likes.all().count()
        return total_liked

    

def save(self, *args, **kwargs):
    super().save(*args, **kwargs)


    img = Image.open(self.image.path)

    if img.height > 300 or img.width > 300:
        output_size = (300,300) 
        img.thumbnail(output_size)
        img.save(self.image.path)


STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted','accepted')
)

class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name="sender")
    reciever = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name="reciever")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES )
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.sender} - {self.reciever} - {self.status}"





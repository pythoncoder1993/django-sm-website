from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.caption

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
    
class UserAddressInformation(models.Model):
    user = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=6, default="")

    def __str__(self):
        return self.address
    
class MarkSheetInformation(models.Model):

    CHOICE_OPTIONS = (

        ('Good', 'Good'),

        ('Average', 'Average'),

        ('Below Average', 'Below Average'),

    )

    user_name = models.CharField(max_length=20)

    math_marks = models.IntegerField()

    english_marks = models.IntegerField()

    teacher_marks = models.CharField(max_length=20, choices=CHOICE_OPTIONS)

    is_sports_team_member = models.BooleanField(default=False)

class SampleMarkSheetInformation(models.Model):

    class TeacherRatingChoices(models.TextChoices):
        Good = 1
        Average = 2
        BelowAverage = 3
    
    user_name = models.CharField(max_length=20)
    math_marks = models.IntegerField()
    english_marks = models.IntegerField()
    teacher_marks_choices = models.CharField(max_length=30, choices=TeacherRatingChoices.choices, default=1)
    is_sports_team_member = models.BooleanField(default=False)

class Article(models.Model):
    article_title = models.CharField(max_length=100, default='')
    article_description = models.CharField(max_length=500, default='')
    is_article_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.article_title

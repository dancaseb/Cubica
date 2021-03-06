from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#User that published the Post or Comment, extended Django User model

class Achievement(models.Model):
    name = models.CharField(max_length=200, default='name')
    achievement_text = models.CharField(max_length=200)
    achievement_points = models.IntegerField()
    def __str__(self):
        return self.achievement_text

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #achievements = models.ForeignKey(Achievement,on_delete=models.CASCADE, default=1)
    achievements = models.ManyToManyField(Achievement)
    profile_pic = models.ImageField(upload_to ='static/cubica/profile_images',default='static/cubica/profile_images/default_profile.jpg')
    bio = models.CharField(max_length=400, default = '')

    def __str__(self):
        return self.user.username

#The SubCubes model
class SubCube(models.Model):
    subname = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created')
    people = models.ManyToManyField(Person)
    subcube_pic = models.ImageField(upload_to ='static/cubica/other',default='static/cubica/other/group.png')
    description = models.CharField(max_length=400, default='')
    def __str__(self):
        return self.subname

class Post(models.Model):
    post_name = models.CharField(max_length=100)
    post_text = models.CharField(max_length=1200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    person = models.ForeignKey(Person,on_delete=models.CASCADE,default=1)
    pic = models.ImageField(upload_to ='static/cubica/images',default=None)
    subcube = models.ForeignKey(SubCube,on_delete=models.CASCADE,default = None)
    def __str__(self):
        return self.post_text








class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',auto_now_add=True)
    person = models.ForeignKey(Person,on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.comment_text







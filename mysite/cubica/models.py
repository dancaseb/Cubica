from django.db import models

# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=200)
    created_at = models.DateTimeField('created_at')
    
    def __str__(self):
        return self.username

class Post(models.Model):
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True,)
    
    def __str__(self):
        return self.post_text


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #person = models.OneToOneField(Person, on_delete=models.CASCADE,primary_key=True,)

    def __str__(self):
        return self.comment_text



from django.db import models
from cubica.models import Person,Post
# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(Person,related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Person,related_name='receiver', on_delete=models.CASCADE)
    shared_post = models.ForeignKey(Post,on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    sent_date = models.DateTimeField('date sent', auto_now_add=True)
    pass
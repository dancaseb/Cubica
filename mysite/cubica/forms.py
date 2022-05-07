from django import forms
from .models import Comment,Post

 
# creating a form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post', 'person']

    


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['person', 'subcube'] 

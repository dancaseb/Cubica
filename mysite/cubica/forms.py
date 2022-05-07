from django import forms
from .models import Comment,Post

 
# creating a form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post', 'person']

    


class PostForm(forms.ModelForm):
    post_text = forms.CharField(label="Your Post",widget=forms.Textarea())
    class Meta:
        model = Post
        exclude = ['person', 'subcube'] 

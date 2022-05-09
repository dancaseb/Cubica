from django import forms
from .models import Comment, Post, SubCube
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# creating a form


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post', 'person']


class PostForm(forms.ModelForm):
    post_text = forms.CharField(label="Your Post", widget=forms.Textarea())

    class Meta:
        model = Post
        labels = {
            "pic": "Your Picture"
        }

        exclude = ['person', 'subcube']


class AddToGroup(forms.ModelForm):

    class Meta:
        model = SubCube
        fields = []



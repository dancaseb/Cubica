from django import forms
from .models import Message
class ShareForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['sender', 'shared_post']


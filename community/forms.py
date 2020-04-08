from django.forms import ModelForm
from django import forms
from .models import Comments,Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        widgets = {
            'content': forms.Textarea()          
        }
        fields = ['title','community_type','content','image','tags']

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
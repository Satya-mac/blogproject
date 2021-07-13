from django import forms
from django.db import models
from django.db.models import fields
from django.forms.forms import Form
from blog.models import Comment


class EmailSendForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

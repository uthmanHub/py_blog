from django import forms
from . import models

class createPost(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ['title', 'description', 'content', 'image']
        labels = {
            'title': 'Blog Title',
            'description': 'Blog Description',
            'content': 'Blog Content',
            'image': 'Blog Image'}
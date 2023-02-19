from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    """
    form for managing crud for blogs
    """
    class Meta:
        model = Blog
        fields = '__all__'

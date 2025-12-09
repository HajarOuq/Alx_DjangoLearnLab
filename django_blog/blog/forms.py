from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment,Tag

# Extend UserCreationForm to include email and basic validation
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email


# Simple profile update form (edit first/last name and email)
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

class PostForm(forms.ModelForm):
    # User enters tags as comma-separated string in this field
    tags_field = forms.CharField(
        required=False,
        help_text="Enter comma-separated tags (e.g. django, python)."
    )

    class Meta:
        model = Post
        fields = ['title', 'content']
    
    def __init__(self, *args, **kwargs):
        # When editing, pre-fill tags_field with existing tag names
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            tag_names = ', '.join([t.name for t in self.instance.tags.all()])
            self.fields['tags_field'].initial = tag_names

    def save(self, commit=True):
        # Save Post instance first, then handle tags
        post = super().save(commit=commit)
        tags_val = self.cleaned_data.get('tags_field', '')
        # Parse comma-separated tags, strip whitespace, ignore empties
        tag_names = [t.strip() for t in tags_val.split(',') if t.strip()]
        # Clear existing tags and re-add (simpler)
        post.tags.clear()
        for name in tag_names:
            tag, created = Tag.objects.get_or_create(name__iexact=name, defaults={'name': name})
            # get_or_create with case-insensitive lookup above tries to avoid duplicates;
            # but if your DB doesn't support case-insensitive get_or_create, you can use:
            # tag, created = Tag.objects.get_or_create(name=name)
            post.tags.add(tag)
        return post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        data = self.cleaned_data.get('content', '').strip()
        if not data:
            raise forms.ValidationError("Comment cannot be empty.")
        return data
    

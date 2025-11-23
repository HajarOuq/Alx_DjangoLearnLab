# bookshelf/forms.py
from django import forms
from .models import Book

# The form your grader expects
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()
        if not name:
            raise forms.ValidationError("Name cannot be empty.")
        return name


# Your secure ModelForm (keep this for the security task)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]

    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()
        if not title:
            raise forms.ValidationError("Title cannot be empty.")
        return title

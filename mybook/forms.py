from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'desc']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'css_input'}),
            'desc': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }
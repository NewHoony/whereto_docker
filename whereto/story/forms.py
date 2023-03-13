from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        field = ('site_name','site_url','site_con','site_cover')
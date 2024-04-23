from django import forms
from .models import *
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'photo_book': forms.FileInput(attrs={'class':'form-control'}),
            'photo_author': forms.FileInput(attrs={'class':'form-control'}),
            'pages': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
            'rental_price_day': forms.TextInput(attrs={'class':'form-control', 'id':'rentalprice'}),
            'rental_period': forms.TextInput(attrs={'class':'form-control', 'id':'rentaldays'}),
            'total_rental': forms.TextInput(attrs={'class':'form-control', 'id':'totalrental'}),
            'active': forms.CheckboxInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
        }
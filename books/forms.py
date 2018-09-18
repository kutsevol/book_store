from django import forms
from django.forms import ModelForm

from .models import Books


class DateInput(forms.DateInput):
    input_type = 'date'


class EditBookForm(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        widgets = {
            'published_date': DateInput(),
        }

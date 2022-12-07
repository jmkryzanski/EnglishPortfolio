from django.forms import ModelForm
from .models import Contact
from django import forms

'''class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
'''

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('email', 'subject', 'message')
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'form-control form-input' ,
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control form-input' ,
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control form-input',
                'rows': 5,
            }),
        }
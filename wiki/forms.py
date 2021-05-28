from django import forms
from .models import Page
from django.contrib.auth.forms import UserCreationForm

class PageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['content'].widget.attrs.update({'class':'form-control'})


    class Meta:
        model = Page
        fields = ("title", "content", "image",)

class Login(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
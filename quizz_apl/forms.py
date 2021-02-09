from django import forms
from django.forms import TextInput
from django.contrib import admin
from quizz_apl.models import Quiz,Question
from django.contrib.auth.models import User




class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'description']

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name of the Quiz', 'class': 'form-control'}),
            'description': TextInput(attrs={'placeholder': 'Description for the Quiz', 'class': 'form-control'}),
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['label']

        widgets = {
            'label': TextInput(attrs={'placeholder': 'Name of the Quiz', 'class': 'form-control'}),
            }
    def __init__(self, pk, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.pk = pk

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name','email','password']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Name of the Quiz', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Name of the Quiz', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Name of the Quiz', 'class': 'form-control'}),
            'password': TextInput(attrs={'placeholder': 'Description for the Quiz', 'class': 'form-control'}),
        }



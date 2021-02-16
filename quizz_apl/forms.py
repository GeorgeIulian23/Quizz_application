from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import TextInput
from django.contrib import admin
from quizz_apl.models import Quiz,Question,QuizTakers,Answer
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


class QuizTaker(forms.ModelForm):


    class Meta:
        model = QuizTakers
        fields=['user','quiz','correct_answers']
        widgets = {
            'user': TextInput(attrs={'placeholder': 'Name of the Quiz', 'class': 'form-control'}),
            'quiz': TextInput(attrs={'placeholder': 'Name of the Quiz', 'class': 'form-control'}),
            'correct_answers': TextInput(attrs={'placeholder': 'Name of the Quiz', 'class': 'form-control'}),

        }



class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer

        fields = "__all__"
    for i in range(1, 50):

        f"label_{i} = forms.TextInput()"
        f"asnwer1_{i} = forms.Checkbox()"
        f"asnwer2_{i} = forms.Checkbox()"
        f"asnwer3_{i} = forms.Checkbox()"
        f"asnwer4_{i} = forms.Checkbox()"
        f"text_asnwer1_{i} = forms.Checkbox()"
        f"text_asnwer2_{i} = forms.Checkbox()"
        f"text_asnwer3_{i} = forms.Checkbox()"
        f"text_asnwer4_{i} = forms.Checkbox()"

    def clean(self):
        cleaned_data = self.cleaned_data
        for i in range(1, 50):
            self.cleaned_data.update({f"label_{i}":self.data.get(f"label_{i}"),f"asnwer1_{i}":self.data.get(f"asnwer1_{i}")})
        return cleaned_data



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']
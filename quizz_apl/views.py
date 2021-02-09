from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import ListView,CreateView
from quizz_apl.models import Quiz,Question,Answer
from quizz_apl.forms import QuizForm, QuestionForm
from django.urls import reverse
import random



class QuizListView(ListView):
    model = Quiz
    template_name = 'quizz/Quizz_lists.html'
    context_object_name = 'all_quizzez'

    def get_queryset(self):
        queryset = super(QuizListView, self).get_queryset()
        return queryset.filter(description=False)

class QuestionView(ListView):
    model = Question
    template_name = 'quizz/home_index.html'
    context_object_name = 'all_questions'


class Create(CreateView):
    model = Quiz
    template_name = 'quizz/home_adauga.html'
    form_class = QuizForm
    def get_form_kwargs(self):
        kwargs = super(Create, self).get_form_kwargs()
        kwargs.update({'pk': None})
        return kwargs

    def get_success_url(self):
        return reverse('quizz:home')


class AnswerView(LoginRequiredMixin,ListView):
    model = Answer
    template_name = 'quizz/home_index.html'
    context_object_name = 'all_answers'

    def clean(self):
        cleaned_data = self.cleaned_data


def index(request):
    quizzez = Quiz.objects.all()
    print(quizzez)
    context = {'quizzez':quizzez}
    return render(request,'quizz/home.html',context)

# def see_question(request):
#     questions=Question.objects.all()
#     if request.method == "GET":
#         if Quiz.objects.filter(p)
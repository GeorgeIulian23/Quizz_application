from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm

# Create your views here.
from django.template.context_processors import request
from django.views.generic import ListView, CreateView
from quizz_apl.models import Quiz, Question, Answer, QuizTakers
from quizz_apl.forms import QuizForm, QuestionForm, QuizTaker, AnswerForm
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


class AnswerView(LoginRequiredMixin, ListView):
    model = Answer
    template_name = 'quizz/home_index.html'
    context_object_name = 'all_answers'

    def get_queryset(self):
        items = Answer.objects.filter(question__quiz_id=self.kwargs['pk'])

        return list(items)

    # imi returneaza toate raspunsurile id ului dat dar static.. nu dinamic

    def get_success_url(self):
        return reverse('quizz:add', kwargs={'pk': self.object.pk})


def index(request):
    quizzez = Quiz.objects.all()
    context = {'quizzez': quizzez}
    return render(request, 'quizz/home.html', context)


class New_quiz_Taker(LoginRequiredMixin, CreateView):
    model = QuizTakers
    template_name = 'quizz/quiz_taker.html'
    form_class = QuizTaker

    def get_success_url(self,*args):
        return reverse("quizz:quiz_ans",args=[self.request.GET.get('quiz')])

    def get_context_data(self, **kwargs):
        data = super(New_quiz_Taker, self).get_context_data(**kwargs)
        data['answer_objects'] = Answer.objects.filter(question__quiz_id=self.request.GET.get('quiz'))
        return data

    def form_invalid(self, form):
        print(form.errors)
        return super(New_quiz_Taker, self).form_invalid(form)

    def form_valid(self, form):
        print('form')
        answer_form = AnswerForm(self.request.POST)
        print(answer_form.errors)

        for i in range(1, 50):
            print(answer_form.cleaned_data[f"asnwer1_{i}"])
            print(answer_form.cleaned_data[f"label_{i}"])

            if answer_form.cleaned_data[f"label_{i}"] is not None:
                if QuizTakers.objects.filter(user_id=self.request.user.id,
                                             quiz_id=Question.objects.get(label=answer_form.cleaned_data[f"label_{i}"]).id).exists() is False:
                    if Answer.objects.filter(text=answer_form.cleaned_data[f"asnwer1_{i}"], is_correct=1).exists():
                        QuizTakers.objects.create(quiz_id=Question.objects.get(label=answer_form.cleaned_data[f"label_{i}"]).quiz_id,
                                                  answer=Answer.objects.get(text=answer_form.cleaned_data[f"asnwer1_{i}"]),
                                                  user_id = self.request.user.id,correct_answers=1)
                    else:
                        QuizTakers.objects.create(quiz_id=Question.objects.get(label=answer_form.cleaned_data[f"label_{i}"]).quiz_id,
                                                  answer=Answer.objects.get(text=answer_form.cleaned_data[f"asnwer1_{i}"]),
                                                  user_id = self.request.user.id,correct_answers=0)
        return super(New_quiz_Taker, self).form_valid(form)



class ListareRaspuns(LoginRequiredMixin,ListView):
    model = QuizTakers
    template_name = 'quizz/quiz_ans.html'
    form_class = QuizTaker

    # def get_correct(self):
    #     rezultat = 0
    #     print(QuizTaker.objects.filter(correct_answers=1))
    #     if QuizTakers.objects.filter(user_id=self.request.user.id).exists():
    #         data=QuizTakers.objects.filter(correct_answers=1)
    #         print(data)
    #         return data

    def get_success_url(self):
        return reverse("quizz:home")



    def get_context_data(self, **kwargs):
        rezultat = 0
        items = super(ListareRaspuns, self).get_context_data(**kwargs)
        items['correct'] = QuizTakers.objects.filter(correct_answers=1,quiz_id=self.kwargs['pk'],user_id=self.request.user.id).values('correct_answers')

        for i in items['correct']:
            for value in i.values():
                if value ==1:
                    rezultat+=1

        items['rezultat'] = rezultat * 10 * 2
        return items

def registerPage(request):
    form = CreateUserForm()


    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quizz:login')

    context = {'form':form}
    return render(request,'quizz/register.html',context)

def loginPage(request):
    context ={}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("quizz:homee")
        else:
            messages.info(request,"user or pass incorrect")
    return render(request,'quizz/login.html',context)

def logout(request):
    logout(request)
    return redirect('quizz:login')
### get raspunsurile corecte ale utilizatorului si aduna raspunsurile + facut grafic cu userii pentru admin
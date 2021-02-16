from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

class Subject(models.Model):
    subject = models.CharField(max_length=50)

class Quiz(models.Model):
    name = models.CharField(max_length=1000)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    questions_count = models.IntegerField(default=0)
    description = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    label = models.CharField(max_length=1000)

    def __str__(self):
        return self.label

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=1000, null=True, blank=True)
    is_correct = models.IntegerField(default=1,null=True,blank=True)

    def __str__(self):
        return self.text


class QuizTakers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    quiz = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    correct_answers = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Response(models.Model):
    quiztaker = models.ForeignKey(QuizTakers, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.question.label
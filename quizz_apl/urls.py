from django.urls import path
from quizz_apl import views

app_name = 'quizz'
urlpatterns = [
    path('',views.index,name='homee'),
    path('quiz/',views.AnswerView.as_view(), name = 'quiz_view'),

    path('',views.QuestionView.as_view(), name = 'home'),
    path('',views.Create.as_view(), name = 'home'),
    path('home_adauga/',views.Create.as_view(), name = 'add')
]
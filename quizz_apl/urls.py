from django.urls import path
from quizz_apl import views

app_name = 'quizz'
urlpatterns = [
    path('',views.index,name='homee'),
    path('logout/',views.logout,name='logout'),
    path('login/',views.loginPage,name='login'),
    path('register/',views.registerPage,name='register'),
    path('quiz/<int:pk>/',views.AnswerView.as_view(), name = 'quiz_view'),
    path('',views.QuestionView.as_view(), name = 'home'),
    path('',views.Create.as_view(), name = 'home'),
    path('home_adauga/',views.Create.as_view(), name = 'add'),
    path('quiz_taker/',views.New_quiz_Taker.as_view(), name = 'quizz'),
    path('quiz_taker/answer/<int:pk>/',views.ListareRaspuns.as_view(), name = 'quiz_ans')

]
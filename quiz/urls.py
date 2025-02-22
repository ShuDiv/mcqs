from django.urls import path, re_path
from quiz.views import MyQuizListAPI, QuizListAPI, QuizDetailAPI, SaveUsersAnswer, SubmitQuizAPI


urlpatterns = [
# 	# path("my-quizzes/", MyQuizListAPI.as_view()),
# 	# path("quizzes/", QuizListAPI.as_view()),
	path("save-answer/", SaveUsersAnswer.as_view()),
# 	# re_path(r"quizzes/(?P<slug>[\w\-]+)/$", QuizDetailAPI.as_view()),
	re_path(r"quizzes/submit/$", SubmitQuizAPI.as_view()),
]
from django.db import models
from django.contrib.auth.models import User
from quiz.models import *
from question.models import *
# Create your models here.

class userQuiz(models.Model):
    quiz_user = models.ManyToManyField(User)
    quiz_object = models.ManyToManyField(quizC)
    quiz_marks_obtained = models.IntegerField()

class userQuestionMarks(models.Model):
    quiz_user_object = models.ManyToManyField(userQuiz)
    ques_object = models.ManyToManyField(ques)
    ques_marks_obtained = models.IntegerField()

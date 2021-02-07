from django.db import models
from question.models import *
import datetime

# Create your models here.

class quizSubSubject(models.Model):
    sub_subject_title = models.CharField(max_length=50)
    sub_subjects_questions = models.ManyToManyField(ques)

class quizSubject(models.Model):
    subject_title = models.CharField(max_length=50)
    sub_subject_objects = models.ManyToManyField(quizSubSubject)

class quizC(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    quiz_title = models.CharField(max_length=50)
    quiz_desc = models.CharField(max_length=200)
    quiz_total_marks = models.IntegerField(default=0)
    subjects_objects = models.ManyToManyField(quizSubject)
    maxTime = models.DurationField(default=datetime.timedelta(hours=1))
    
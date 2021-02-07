from django.db import models

class ques(models.Model):
    ques_id = models.AutoField(primary_key=True)
    ques_title = models.CharField(max_length=50)
    ques_desc = models.CharField(max_length=200)
    ques_marks = models.IntegerField()

class mcq_option(models.Model):
    option_desc = models.CharField(max_length=50)
    is_ans = models.BooleanField(default=False)

class mcq(models.Model):
    ques_object = models.ForeignKey(ques,on_delete=models.CASCADE)
    no_of_options = models.IntegerField()
    mcq_option_objects = models.ManyToManyField(mcq_option)

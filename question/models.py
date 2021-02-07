from django.db import models

TYPE_OF_QUESTIONS_CHOICE = (
    ('MCQ','MCQ'),
    ('TF','TF'),
    ('IntegerType','IntegerType')
)
class ques(models.Model):
    ques_id = models.AutoField(primary_key=True)
    ques_title = models.CharField(max_length=50)
    ques_desc = models.CharField(max_length=200)
    ques_type = models.CharField(choices=TYPE_OF_QUESTIONS_CHOICE,default='MCQ')
    ques_marks = models.IntegerField(default=0)
    ques_reason = models.CharField(max_length=200)

class mcq_option(models.Model):
    mcq_option_id = models.AutoField(primary_key=True)
    option_desc = models.CharField(max_length=50)
    is_ans = models.BooleanField(default=False)

class mcq(models.Model):
    ques_object = models.ForeignKey(ques,on_delete=models.CASCADE)
    no_of_options = models.IntegerField(default = 0)
    mcq_option_objects = models.ManyToManyField(mcq_option)

class tf(models.Model):
    ques_object = models.ForeignKey(ques,on_delete=models.CASCADE)
    tf_ans = models.BooleanField(default=False)

class integerType(model.Models):
    ques_object = models.ForeignKey(ques,on_delete=models.CASCADE)
    integerType_ans = models.IntegerField(default= 0)
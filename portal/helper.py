from django.contrib.auth.models import User
from quiz.models import *
from question.models import *
from .models import *

def quizReportHelper(response):
    tf_dict = {
        1: True,
        0:False
    }
    newUserQuizRecord = userQuiz(
        quiz_user=request.user,
        quiz_object=quizC.objects.all().filter(response['quiz_id']),
        quiz_marks_obtained = 0
    )
    newUserQuizRecord.save()
    for ques_id,option_id in response.items():
        ques_object = ques.objects.all().filter(ques_id = ques_id)[0]
        alloted_marks = 0
        if ques_object.ques_type == 'MCQ':
            if mcq_option.objects.all().filter(mcq_option_id = option_id)[0].is_ans:
                alloted_marks = ques_object.ques_marks
        elif ques_object.ques_type == 'TF':
            if tf.objects.all().filter(ques_object=ques_object)[0].tf_ans == tf_dict[option_id]:
                alloted_marks = ques_object.ques_marks
        else:
            if integerType.objects.all().filter(ques_object = ques_object)[0].integerType_ans == int(option_id):
                alloted_marks = ques_object.ques_marks

        newQuesRecord = userQuestionMarks(
            ques_object=ques_object,
            ques_marks_obtained = alloted_marks
        )
        newQuesRecord.save()
        newUserQuizRecord.userquestionmarks_set.add(newQuesRecord)
        newUserQuizRecord.quiz_marks_obtained += newQuesRecord
        newUserQuizRecord.save()




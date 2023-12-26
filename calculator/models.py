import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class MathematicalProblem(models.Model):
    creation_time = models.DateTimeField('date published')
    problem_description = models.CharField(max_length=250)

    def __str__(self):
        return self.problem_description

    def was_published_recently(self):
        return self.creation_time >= timezone.now() - datetime.timedelta(days=1)


class Answer(models.Model):
    question = models.ForeignKey(MathematicalProblem, on_delete=models.CASCADE)
    user_ans = models.IntegerField(default=0)
    answer = models.CharField(max_length=40)
    answer_description = models.CharField(max_length=250)

    def __str__(self):
        return self.answer

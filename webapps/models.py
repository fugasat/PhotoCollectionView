import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField('質問', max_length=200)
    pub_date = models.DateTimeField('公開日')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('選択肢', max_length=200)
    votes = models.IntegerField('投票数', default=0)

    def __str__(self):
        return self.choice_text
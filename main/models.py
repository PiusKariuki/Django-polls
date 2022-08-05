from datetime import timedelta, datetime

from django.db import models


# Create your models here.
def ensure_datetime(d):
    """
    Takes a date or a datetime as input, outputs a datetime
    """
    if isinstance(d, datetime):
        return d
    return datetime(d.year, d.month, d.day)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('Date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        split = datetime.now() - timedelta(days=1)
        # print(f"pubdate {self.pub_date}")
        # print(f"date time  pub date{ensure_datetime(self.pub_date)}")
        # print(f"split {split}")
        # print(f"Date time split {split}")
        return ensure_datetime(self.pub_date) >= ensure_datetime(split)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

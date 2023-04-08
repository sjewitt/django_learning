import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') #? - OK, it is optional first(huh?) arg as human-eadable field, otherwise defaults to variable name

    # add a magic function to return the string representation of this class:
    # this means that implicitly calling __str__ will not list <QuerySet [<Question: Question object (1)>]>,
    # but the actual value:
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    
    # how does it know WHICH is the FK field? Is there an auto-id added - er - automatically?
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # add a magic function to return the string representation of this class:
    def __str__(self):
        return self.choice_text

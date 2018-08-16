import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    text = models.CharField(max_length=200)
    date_published = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        # return self.date_published >= timezone.now() - datetime.timedelta(days=1)
        return now - datetime.timedelta(days=1) <= self.date_published <= now

    was_published_recently.admin_order_field = 'date_published'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.text

    class Meta:
        db_table = "Polls_Question"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.text

    class Meta:
        db_table = "Polls_Choice"


from django.db import models


# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=50)



    parament_tag = models.ForeignKey(
        'self', null=True, blank=True, related_name='child_tag',
         on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Question(models.Model):
    question_text=models.CharField(max_length=200)
    answer_text=models.CharField(max_length=50)
    tag = models.ForeignKey(Tag, null=True, blank=True,
                           related_name='Tag', on_delete=models.CASCADE)
    def __str__(self):
        return self.question_text


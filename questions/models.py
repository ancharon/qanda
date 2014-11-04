from django.db import models

class Question(models.Model):
    """
    Model for Question objects, which include some question text
    and a number of potential Answers as children.
    """
    ADDITION = 'addition'
    SUBTRACTION = 'subtraction'
    MULTIPLICATION = 'multiplication'
    DIVISION = 'division'
    QUESTION_TYPES = (
        (ADDITION, 'addition'),
        (SUBTRACTION, 'subtraction'),
        (MULTIPLICATION, 'multiplication'),
        (DIVISION, 'division'),
    )
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=100, blank=False, default='')
    type = models.CharField(choices=QUESTION_TYPES,
                            blank=False,
                            default=ADDITION,
                            max_length=50)
     
    class Meta:
        ordering = ('created',)

class Answer(models.Model):
    """
    Model for Answer objects, which are tied to a parent Question.
    Answers can be correct or incorrect.
    """
    created = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=19, decimal_places=10)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey('Question', related_name='answers')
    
    class Meta:
        ordering = ('created',)
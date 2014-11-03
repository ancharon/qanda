from django.db import models

class Question(models.Model):
    ADDITION = 'ADD'
    SUBTRACTION = 'SUB'
    MULTIPLICATION = 'MUL'
    DIVISION = 'DIV'
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
    created = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=19, decimal_places=10)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey('Question', related_name='answers')
    
    class Meta:
        ordering = ('created',)
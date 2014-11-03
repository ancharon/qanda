from questions.models import Question, Answer
from questions.serializers import QuestionSerializer, AnswerSerializer
from rest_framework import viewsets

class QuestionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
        
        
class AnswerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
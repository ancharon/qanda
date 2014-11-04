from questions.models import Question, Answer
from questions.serializers import QuestionSerializer, AnswerSerializer
from rest_framework import viewsets, filters

class QuestionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # Specify which fields to use for filtering, searching, and ordering
    filter_fields = ('text', 'type',)
    search_fields = ('text',)
    ordering_fields = ('text', 'type',)
    

class AnswerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    # Specify which fields to use for filtering and ordering
    filter_fields = ('value', 'is_correct',)
    ordering_fields = ('value', 'is_correct',)
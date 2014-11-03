from rest_framework import serializers
from questions.models import Question, Answer

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    question = serializers.Field(source='question.text')

    class Meta:
        model = Answer
        fields = ('url', 'value', 'is_correct', 'question')
    
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers = serializers.HyperlinkedRelatedField(many=True, view_name='answer-detail')

    class Meta:
        model = Question
        fields = ('url', 'text', 'type', 'answers')
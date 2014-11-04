from rest_framework import serializers
from questions.models import Question, Answer

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for questions.models.Answer
    """
    question = serializers.Field(source='question.text')
    
    # TODO: need to get the request here somehow to reverse the url, since apparently can't just do this
    # question_url = serializers.Field(source='question.url')
    
    # hacking this for now...
    question_url = serializers.SerializerMethodField('get_question_url')
    def get_question_url(self, obj):
        return "http://127.0.0.1:8000/questions/%d/" % obj.question.id

    class Meta:
        model = Answer
        fields = ('url', 'value', 'is_correct', 'question', 'question_url')
    
class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for questions.models.Question
    """
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('url', 'text', 'type', 'answers')
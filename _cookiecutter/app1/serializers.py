from rest_framework.serializers import  HyperlinkedModelSerializer
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer
from .models import Question, Answer

class QuestionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date')


class AnswerSerializer(NestedHyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'answer_text')
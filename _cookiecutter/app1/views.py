from rest_framework import viewsets
from rest_framework import mixins
from .serializers import QuestionSerializer, AnswerSerializer
from .models import Question, Answer

class QuestionModelViewSet(mixins.CreateModelMixin,
                           mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    """
    A viewset for viewing and editing question instances.
    """
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class AnswerModelViewSet(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    """
    A viewset for viewing and editing answer instances.
    """
    serializer_class = AnswerSerializer
    def get_queryset(self):
        return Answer.objects.filter(question=self.kwargs['question_pk'])

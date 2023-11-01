# urls.py
from rest_framework_nested import routers
from .views import QuestionModelViewSet, AnswerModelViewSet
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'questions', QuestionModelViewSet)

domains_router = routers.NestedSimpleRouter(router, r'questions', lookup='question')
domains_router.register(r'answers', AnswerModelViewSet, basename='question-answers')
# 'basename' is optional. Needed only if the same viewset is registered more than once
# Official DRF docs on this option: http://www.django-rest-framework.org/api-guide/routers/

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(domains_router.urls)),
]
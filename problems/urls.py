from django.urls import path, include
from rest_framework.routers import DefaultRouter

from problems.views import QuestionViewSet, AnswerViewSet

question_router = DefaultRouter(trailing_slash=False)
question_router.register('questions', QuestionViewSet, basename='questions')

answer_router = DefaultRouter(trailing_slash=False)
answer_router.register('answers', AnswerViewSet, basename='answers')

urlpatterns = [
    path('', include(question_router.urls)),
    path('', include(answer_router.urls)),
]
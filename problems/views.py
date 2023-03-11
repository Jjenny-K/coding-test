from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, filters
from rest_framework.response import Response

from problems.models import Question, Answer
from problems.serializers import QuestionCreateSerializer, \
                                 QuestionListSerializer, \
                                 QuestionDetailSerializer, \
                                 AnswerCreateSerializer, \
                                 AnswerListSerializer, \
                                 AnswerDetailSerializer
from problems.permissions import QuestionIsOwnerOrReadOnly, AnswerIsOwner


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return QuestionListSerializer
        elif self.action == 'create':
            return QuestionCreateSerializer
        else:
            return QuestionDetailSerializer

    permission_classes = (QuestionIsOwnerOrReadOnly,)

    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    search_fields = ('title', 'category', 'difficulty',)
    ordering_fields = ('created_at',)

    def get_product(self, pk):
        return get_object_or_404(Question, id=pk)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # 로그인된 사용자 정보를 추가해 Question 생성
            Question.objects.create(
                user_id=request.user.id,
                title=request.data['title'],
                description=request.data['description'],
                constraint=request.data['constraint'],
                category=request.data['category'],
                difficulty=request.data['difficulty'],
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AnswerListSerializer
        elif self.action == 'create':
            return AnswerCreateSerializer
        else:
            return AnswerDetailSerializer

    permission_classes = (AnswerIsOwner,)

    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    search_fields = ('question__title', 'question__category', 'question__difficulty',)
    ordering_fields = ('created_at',)

    def get_product(self, pk):
        return get_object_or_404(Answer, id=pk)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # 로그인된 사용자 정보를 추가해 Answer 생성
            Answer.objects.create(
                user_id=request.user.id,
                question=request.data['question'],
                answer=request.data['answer'],
                description=request.data['description'],
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import serializers

from problems.models import Question, Answer


class QuestionCreateSerializer(serializers.ModelSerializer):
    """ 문제 생성 serializer """
    class Meta:
        model = Question
        fields = (
            'title',
            'description',
            'constraint',
            'category',
            'difficulty',
        )


class QuestionListSerializer(serializers.ModelSerializer):
    """ 문제 목록 serializer """
    class Meta:
        model = Question
        fields = (
            'id',
            'category',
            'title',
        )


class QuestionDetailSerializer(serializers.ModelSerializer):
    """ 문제 상세 serializer """
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Question
        fields = (
            'username',
            'title',
            'description',
            'constraint',
            'category',
            'difficulty',
        )


class AnswerCreateSerializer(serializers.ModelSerializer):
    """ 답안 및 해설 생성 serializer """
    class Meta:
        model = Answer
        fields = (
            'question',
            'answer',
            'description',
        )


class AnswerListSerializer(serializers.ModelSerializer):
    """ 답안 및 해설 목록 serializer """
    question_category = serializers.ReadOnlyField(source='question.category')
    question_title = serializers.ReadOnlyField(source='question.title')

    class Meta:
        model = Answer
        fields = (
            'id',
            'category',
            'title',
        )


class AnswerDetailSerializer(serializers.ModelSerializer):
    """ 답안 및 해설 상세 serializer """
    user_name = serializers.ReadOnlyField(source='user.username')
    question_title = serializers.ReadOnlyField(source='question.title')
    question_description = serializers.ReadOnlyField(source='question.description')

    class Meta:
        model = Answer
        fields = (
            'username',
            'question_title',
            'question_description',
            'answer',
            'description',
        )

from django.db import models

from utils.timestamp import TimestampZone


class Question(TimestampZone):
    user = models.ForeignKey('accounts.User', verbose_name='작성자', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='문제명', max_length=255)
    description = models.TextField(verbose_name='문제설명')
    constraint = models.TextField(verbose_name='제한사항', blank=True, default='')
    category = models.CharField(verbose_name='유형', max_length=31)

    class DifficultyType(models.TextChoices):
        EASY = 'EASY'
        NORMAL = 'NORMAL'
        HARD = 'HARD'

    difficulty = models.CharField(verbose_name='난이도', max_length=15, choices=DifficultyType.choices)

    class Meta:
        db_table = 'question'

    def __str__(self):
        return f'question {self.category}-{self.title}'


class Answer(TimestampZone):
    user = models.ForeignKey('accounts.User', verbose_name='작성자', on_delete=models.CASCADE)
    question = models.ForeignKey('problems.Question', verbose_name='문제', on_delete=models.CASCADE)
    answer = models.CharField(verbose_name='답안', max_length=255)
    description = models.TextField(verbose_name='해설')
    testcase = models.JSONField(verbose_name='테스트케이스', default=dict)

    class Meta:
        db_table = 'answer'

    def __str__(self):
        return f'{self.question} answer'

from django.contrib import admin

from problems.models import Question, Answer

admin.site.register([Question, Answer])

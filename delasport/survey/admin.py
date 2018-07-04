from django.contrib import admin
from models import Survey, Question, Responses


class ResponsesAdmin(admin.StackedInline):
    model = Responses


class QuestionAdmin(admin.ModelAdmin):
    model = Question

    class Meta:
        list_display = ('question_text', 'question_type', 'status', 'created_at')

    inlines = [ResponsesAdmin]


admin.site.register(Question, QuestionAdmin)




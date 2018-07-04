from django import forms
from survey.models import Question


class SurveyForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)
        active_questions = Question.objects.filter(
            status=Question.QUESTION_STATUS_ACTIVE,
        )
        for question in active_questions:
            question_name = 'question_{}'.format(question.number)
            if question not in self.fields:
                if question.type == Question.QUESTION_RATTING:
                    question_choices = (
                        (question_name, response)
                        for response in range(1, Question.QUESTION_RATTING_OPTIONS)
                    )
                    self.fields[question_name] = forms.RadioSelect(
                        choices=question_choices
                    )
                elif question.type == Question.QUESTION_SINGLE_SELECT:
                    question_choices = (
                        (question_name, Question.QUESTION_SINGLE_SELECT_ANSWER_YES),
                        (question_name, Question.QUESTION_SINGLE_SELECT_ANSWER_NO),
                    )
                    self.fields[question_name] = forms.RadioSelect(
                        choices=question_choices
                    )

import random
from django.core.management import BaseCommand
from django.db import transaction
from survey.models import Survey, Answers, Question


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.survey_answers = []
        self.surveys = Survey.objects.all()
        self.answer_id = 1

    def add_answer(self, answer_id, answer, question_id, survey_id):

        self.survey_answers.append(
            Answers(
                id=int(answer_id),
                answer=answer,
                question_id=question_id,
                survey_id=survey_id,
            )
        )

    @transaction.atomic
    def handle(self, *args, **options):
        for index, survey in enumerate(self.surveys):
            survey_id = survey.id

            for question in Question.objects.exclude(
                    status=Question.QUESTION_STATUS_INACTIVE,
            ).order_by(
                'number',
            ):
                if question.question_type == Question.QUESTION_RATTING:
                    self.add_answer(
                        self.answer_id,
                        random.choice(range(1, Question.QUESTION_RATTING_OPTIONS+1)),
                        question.id,
                        survey_id,
                   )
                else:
                    self.add_answer(
                        self.answer_id,
                        random.choice(range(1, 3)),
                        question.id,
                        survey_id,
                    )
                self.answer_id += 1

        Answers.objects.bulk_create(self.survey_answers)
        self.stdout.write(
            self.style.SUCCESS(
                'Successfully added {} survey answers.'.format(len(self.survey_answers))))

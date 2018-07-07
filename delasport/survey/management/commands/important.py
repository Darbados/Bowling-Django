from django.core.management import BaseCommand
from survey.models import Question


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.questions = []

    def add_arguments(self, parser):
        parser.add_argument('number_of_questions', type=int)

    def handle(self, *args, **options):
        num_questions = options['number_of_questions']
        for question_number in range(15000, num_questions):
            question_id = question_number
            question_text = 'This is question {}'.format(question_number)
            question_type = Question.QUESTION_RATTING
            status = Question.QUESTION_STATUS_ACTIVE
            number = question_number

            self.questions.append(
                Question(
                    id=question_id,
                    question_text=question_text,
                    question_type=question_type,
                    status=status,
                    number=number,
                )
            )

        Question.objects.bulk_create(self.questions)
import csv
import json
from django.core.management import BaseCommand

from Store.utils import ActivateLanguage
from surveys.models import Survey, Question, Answer

IMPORT_LANGUAGE_CODE = 'bg'


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.old_questions = {}
        self.current_questions = {
            question.question_text: question.id for question in
            Question.objects.filter(
                status=Question.QUESTION_STATUS_ACTIVE,
            )
        }
        self.not_found_surveys = {'surveys': []}
        self.answers_list = []

    def map_questions(self):
        with open('/home/pesho/Downloads/ebagcore_surveys_question.csv', 'r') as old_questions:
            reader = csv.reader(old_questions, delimiter=',')
            for question in reader:
                question_id, question_text = question
                self.old_questions[question_id] = question_text

    def save_answer(self, answer_id, answer, question_id, survey_id):
        question_text = self.old_questions[question_id]
        new_question_id = self.current_questions[question_text]

        try:
            question = Question.objects.get(pk=new_question_id)
            survey = Survey.objects.get(pk=survey_id)

            self.answers_list.append(
                Answer(
                    id=answer_id,
                    answer=answer,
                    question_id=question.id,
                    survey_id=survey.id,
                )
            )
        except Survey.DoesNotExist:
            self.not_found_surveys['surveys'].append(survey_id)

    def save_not_found_surveys(self, data):
        with open('not_found_surveys_log.json', 'w') as log_file:
            json.dump(data, log_file, ensure_ascii=False)

    def handle(self, *args, **options):
        self.map_questions()

        with ActivateLanguage(IMPORT_LANGUAGE_CODE):
            with open('/home/pesho/Downloads/ebagcore_surveys_answer.csv', 'r') as input_data:
                reader = csv.reader(input_data, delimiter=',')
                for row in reader:
                    answer_id, answer, question_id, survey_id = row

                    self.save_answer(
                        answer_id,
                        answer,
                        question_id,
                        survey_id,
                    )

                Answer.objects.bulk_create(self.answers_list)

                self.stdout.write(
                    self.style.SUCCESS(
                        'Successfully processed {} answers.'.format(len(self.answers_list)))
                )
                self.save_not_found_surveys(self.not_found_surveys)
import csv
from django.core.management import BaseCommand
from survey.models import Survey


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.surveys = []

    def save_survey(self, survey_id, survey_unique_value, status, user_comment, internal_comment,
                    created_at, updated_at):

        self.surveys.append(
            Survey(
                id=int(survey_id),
                survey_unique_value=survey_unique_value,
                status=int(status),
                user_comment=user_comment,
                internal_comment=internal_comment,
                created_at=created_at,
                updated_at=updated_at,
            )
        )

    def handle(self, *args, **options):
        with open('/home/pesho/Projects/Bowling-Django/delasport/survey/db_export/survey_survey.csv', 'r') as input_data:
            reader = csv.reader(input_data, delimiter=',')
            next(reader)
            for row in reader:
                survey_id, survey_unique_value, status, user_comment, internal_comment, created_at, updated_at = row

                self.save_survey(
                    survey_id,
                    survey_unique_value,
                    status,
                    user_comment,
                    internal_comment,
                    created_at,
                    updated_at
               )

            Survey.objects.bulk_create(self.surveys)
            self.stdout.write(
                self.style.SUCCESS(
                    'Successfully processed {} survey records.'.format(len(self.surveys))))

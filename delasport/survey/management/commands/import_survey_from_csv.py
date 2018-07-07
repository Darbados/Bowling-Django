import csv
import json
import pytz
from datetime import datetime
from django.core.management import BaseCommand

from Store.utils import ActivateLanguage
from orders.models import Order
from surveys.models import Survey
from Store.utils import store_today

IMPORT_LANGUAGE_CODE = 'bg'


class Command(BaseCommand):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.not_found_orders = {'orders': []}
        self.counter = 0
        self.surveys = []

    def save_not_found_orders(self, data):
        with open('not_found_orders_log.json', 'w') as log_file:
            json.dump(data, log_file, ensure_ascii=False)

    def make_datetime_aware_of_utc(self, created_at, updated_at):
        created_at = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")
        created_at_aware = created_at.replace(tzinfo=pytz.UTC)
        try:
            updated_at = datetime.strptime(updated_at, "%Y-%m-%d %H:%M:%S")
            updated_at_aware = updated_at.replace(tzinfo=pytz.UTC)
        except ValueError:
            updated_at_aware = None

        return created_at_aware, updated_at_aware

    def save_survey(self, survey_id, created_at, updated_at, survey_unique_value, status, order_id,
                    internal_comment, user_comment):

        created_at_aware, updated_at_aware = self.make_datetime_aware_of_utc(created_at, updated_at)

        try:
            order = Order.objects.get(id=order_id)

            self.surveys.append(
                Survey(
                    id=survey_id,
                    created_at=created_at_aware,
                    updated_at=updated_at_aware,
                    survey_unique_value=survey_unique_value,
                    status=status,
                    order=order,
                    internal_comment=internal_comment,
                    user_comment=user_comment,
                )
            )

            self.counter += 1
        except Order.DoesNotExist:
            self.not_found_orders['orders'].append(order_id)

    def handle(self, *args, **options):
        with ActivateLanguage(IMPORT_LANGUAGE_CODE):
            with open('/home/pesho/Downloads/ebagcore_surveys_survey.csv', 'r') as input_data:
                reader = csv.reader(input_data, delimiter=',')
                for row in reader:
                    survey_id = row[0]
                    survey_unique_value = row[1]
                    user_comment = row[2]
                    created_at = row[3]
                    updated_at = row[4]
                    order_id = row[5]
                    internal_comment = row[6]
                    status = 3 if row[4] != '' else 2

                    self.save_survey(
                        survey_id,
                        created_at,
                        updated_at,
                        survey_unique_value, status,
                        order_id,
                        internal_comment,
                        user_comment,
                    )

                Survey.objects.bulk_create(self.surveys)
                self.stdout.write(
                    self.style.SUCCESS(
                        'Successfully processed {} survey records.'.format(self.counter))
                )
                self.save_not_found_orders(self.not_found_orders)
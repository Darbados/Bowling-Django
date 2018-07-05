import csv

with open('../../survey_question.csv', 'r') as input_data:
    reader = csv.reader(input_data, delimiter=',')
    for row in reader:
        print(row)
import csv

with open('/Users/ryan/Desktop/student_test_scores_extended.xlsx', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')

import openpyxl
from collections import defaultdict

# Load the Excel file
file_path = '/Users/ryan/Desktop/student_test_scores_extended.xlsx'
wb = openpyxl.load_workbook(file_path)

# Select the active sheet (or you can specify the sheet name)
sheet = wb.active

# Initialize a list to hold rows of data
data = []

# Iterate through the rows and collect the data
for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip header row (min_row=2)
    data.append(row)

# Transform the data into a dictionary (assuming the first column is 'Student Name')
students_data = defaultdict(dict)

for row in data:
    student_name = row[0]  # Assuming student name is in the first column
    subject = row[1]  # Assuming subject is in the second column
    score = row[2]  # Assuming score is in the third column

    # Organize the data into a dictionary with the student name as the key
    students_data[student_name][subject] = score

# Now you can access the data as a dictionary
for student, scores in students_data.items():
    print(f"{student}'s scores: {dict(scores)}")
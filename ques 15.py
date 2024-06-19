import csv
with open('students.csv', 'r') as csvf:
    csvreader = csv.reader(csvf)

# Iterating over each row in the CSV file.
for row in csvreader:
  print(row)
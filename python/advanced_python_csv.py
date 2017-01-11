from advanced_python_regex import email
import csv

with open('emails.csv', "w") as file:
    writer = csv.writer(file, lineterminator='\n')
    for e in email:
        writer.writerow([e])

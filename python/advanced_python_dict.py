#Q6 Part III

import csv
with open('faculty.csv', 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)


for d in data[1:len(data)+1]:
    d[0] = d[0].split(" ", 3)[-1]
    d[2] = d[2].split("Professor", 1)[0] + 'Professor'
# print data
t = [tuple(d) for d in data]
faculty_dict = {d[0]: [] for d in t[1:len(t)+1]}
# print faculty_dict

for k in faculty_dict:
    for d in t:
        if k == d[0]:
            faculty_dict[k] += [d[1:]]

print faculty_dict
count = 0
for key in faculty_dict:
    if count < 3:
        print key, faculty_dict[key]
    count += 1

# Q7 Part III

import csv
with open('faculty.csv', 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)
# print data

for d in data[1:len(data)+1]:
    d[0] = [d[0].split(" ", 3)[0] , d[0].split(" ", 3)[-1]]
    d[2] = d[2].split("Professor", 1)[0] + 'Professor'

print data
t1 = [tuple(d) for d in data]

faculty_dict1 = {(d[0][0], d[0][1]): [] for d in t1[1:len(t1)+1]}
print faculty_dict1

for k in faculty_dict1:
    for d in t1:
        if k[1] == d[0][1]:
            faculty_dict1[k] += [d[1:]]

# print faculty_dict1

print(sorted(faculty_dict1.items()))

# Q8 Part III
from operator import itemgetter
print sorted(faculty_dict1, key = itemgetter(1))
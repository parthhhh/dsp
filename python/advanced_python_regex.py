import csv
with open('faculty.csv', 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)
    # print data
    # Print out number of unique degrees, Part 1 of the Question

degree = []
for d in data[1:len(data)+1]:
    if d[1] not in degree:
        degree.append(d[1])
newlist = [newlist.split(" ") for newlist in degree]
nospace = []
for n in newlist:
    for x in range(0, len(n), 1):
        if n[x] <> '' and n[x] <> '0':
            nospace.append(n[x])
s = [s.replace('.', '') for s in nospace]
print set(s)
print 'Number of unique degrees = ' + str(len(set(s)))

# Find out unique titles of the professors, Part 2 of 4

title = []
for d in data[1:len(data)+1]:
    if d[2] not in title:
        title.append(d[2])
n = []
for t in title:
    n.append(t.split('Professor', 1)[0] + 'Professor')
print set(n)
print 'Number of different titles = ' + str(len(set(n)))

# Print list of email addresses, Part 3 of 4

email = []
for d in data[1:len(data)+1]:
    if d[3] not in email:
        email.append(d[3])
print 'List of emails: ' + str(email)

# Print list of different email domains, Part 4 of 4

domain = []
for e in email:
    domain.append(e.split('@', 1)[1])
print set(domain)
print ('Number of different email domain names = ' + str(len(set(domain))))

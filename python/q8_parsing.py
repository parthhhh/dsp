import csv
with open('football.csv', 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)
    goals = []
    goalsa = []
    team = []
    for d in data[1:len(data)+1]:
        goals.append(int(d[5]))
        goalsa.append(int(d[6]))
        team.append(d[0])
    delta = []
    x = 0
    for g in goalsa:
        delta.append(abs(g-goals[x]))
        x = x + 1
    n = delta.index(min(delta))
    answer = team[n]
    print answer
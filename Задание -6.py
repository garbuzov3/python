import re

with open('task-6.txt', 'r') as file:
    lines = file.readlines()
subject_dict = {}

for line in lines:
    parts = line.strip().split(':')
    subject = parts[0].strip()
    details = parts[1].strip().split(' ')
    for detail in details:
        if 'л' in detail or 'пр' in detail or 'лаб' in detail:
            count = int(re.findall(r'\d+', detail)[0])
            if subject in subject_dict:
                subject_dict[subject] += count
            else:
                subject_dict[subject] = count
print(subject_dict)

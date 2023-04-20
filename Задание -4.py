import re

with open('task-4-in.txt', 'r') as task_in, open('task-4-out.txt', 'w') as task_out:
    for line in task_in:
        line = re.sub(r'\bOne\b', 'Один', line)
        line = re.sub(r'\bTwo\b', 'Два', line)
        line = re.sub(r'\bThree\b', 'Три', line)
        line = re.sub(r'\bFour\b', 'Четыре', line)
        task_out.write(line)

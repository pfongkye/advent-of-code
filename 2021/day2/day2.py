import os

SCRIPT_DIR = os.path.dirname(__file__)

# Part 1
forward = 0
depth = 0
with open(os.path.join(SCRIPT_DIR, 'input.txt'),'r',encoding='utf-8') as f:
    for line in f:
        if line.startswith('forward'):
            forward += int(line.split(' ')[1])
        elif line.startswith('up'):
            depth -= int(line.split(' ')[1])
        elif line.startswith('down'):
            depth += int(line.split(' ')[1])

print(f"First result: {forward*depth}")

# Part 2
horizontal = 0
depth = 0
aim = 0

with open(os.path.join(SCRIPT_DIR, 'input.txt'),'r',encoding='utf-8') as f:
    for line in f:
        if line.startswith('forward'):
            forward = int(line.split(' ')[1])
            horizontal += forward
            depth += forward*aim
        elif line.startswith('up'):
            aim -= int(line.split(' ')[1])
        elif line.startswith('down'):
            aim += int(line.split(' ')[1])

print(f"Second result: {horizontal*depth}")

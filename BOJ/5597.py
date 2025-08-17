import sys

students = list(range(1, 31))

for _ in range(28):
    students.remove(int(sys.stdin.readline()))

for i in students:
    print(i)


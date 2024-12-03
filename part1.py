import sys

left_side = []
right_side = []

for line in sys.stdin:
    left, right = line.split()
    left_side.append(int(left))
    right_side.append(int(right))

left_side.sort()
right_side.sort()

total = 0

for l, r in zip(left_side, right_side):
    total += abs(l - r)

print(total)

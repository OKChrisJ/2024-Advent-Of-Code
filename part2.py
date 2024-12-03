import sys
import collections

nums = []
num_counts = collections.Counter()

for line in sys.stdin:
    left, right = [int(n) for n in line.split()]

    nums.append(left)
    num_counts[right] += 1

total = sum(elem * num_counts[elem] for elem in nums)

print(total)

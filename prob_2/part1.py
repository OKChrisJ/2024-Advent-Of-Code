import sys

total = 0

for line in sys.stdin:
    nums_str = line.split()
    nums = [int(n) for n in nums_str]
    increases = nums[0] < nums[-1]

    safe = True

    for i in range(1,len(nums)):
        diff = abs(nums[i] - nums[i-1])
        valid_diff = (diff >= 1) and (diff <= 3)

        if not valid_diff or (increases ^ (nums[i-1] < nums[i])):
            safe = False
            break;

    if safe:
        total += 1
            
print(total)

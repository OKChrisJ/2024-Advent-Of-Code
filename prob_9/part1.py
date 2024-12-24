import sys

def FindFirstDotAndLastNum(code):
    indexOfDot = 0
    indexOfNum = 0

    for i in range(len(code)):
        if code[i] == '.':
            indexOfDot = i
            break
    for i in range(len(code)-1,-1,-1):
        if code[i] != '.':
            indexOfNum = i
            break

    return indexOfDot, indexOfNum

def SwapLastNumberWithDot(code):
    dot = 0
    num = 0
    dot, num = FindFirstDotAndLastNum(code)
    lastNum = code[num]
    code[num] = code[dot]
    code[dot] = lastNum
    return code

def GetCheckSum(code):
    total = 0
    for index, elem in enumerate(code):
        if elem == '.':
            break
        total += (int(elem) * index)
    return total

nums = []

for line in sys.stdin:
    nums = line

code = []
counter = 0
for index, num in enumerate(nums):
    if index == len(nums) - 1:
        break

    for i in range(int(num)):
        if index % 2 == 0:
            code.append(counter)
            if i == int(num) - 1:
                counter += 1
        else:
            code.append('.')

counter = 0
for elem in code:
    if elem == '.':
        counter += 1

for i in range(counter):
    code = SwapLastNumberWithDot(code)

print(GetCheckSum(code))

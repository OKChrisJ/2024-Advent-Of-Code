import sys
import re

elems = []
occurs = []
total = 0

for line in sys.stdin:
    elems.append(line)

for word in elems:
    occurs.append(re.findall("mul([0-9]{3},[0-9)]{3})", word))

for times_func in occurs:
    left_num, right_num = times_func[4:-1].split(',')
    total += left_num * right_num

print(total)
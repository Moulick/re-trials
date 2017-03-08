import re

strings = ['Jan 1987', 'May 1969', 'Aug 2011']

for x in strings:
    matchObj = re.match(r'(\w+\s+(\d+))', x, re.M | re.I)

    if matchObj:
        print("matchObj.group() : ", matchObj.group())
        print("matchObj.group(1) : ", matchObj.group(1))
        print("matchObj.group(2) : ", matchObj.group(2))

    else:
        print("No match!!")
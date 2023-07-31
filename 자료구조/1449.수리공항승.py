
leaks, length = map(int, input().split())
leakPoint = []
for item in map(int, input().split()):
    leakPoint.append(item)

tempEnd = 0
count = 0
leakPoint.sort()

for point in leakPoint:
    if tempEnd < point:
        tempEnd = point + length - 1
        count += 1
    else:
        continue

print(count)

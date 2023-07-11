# Stack으로 풀면 됨

i = int(input())
line = []
for _ in range(i) :
    line.append(input())

for i in range(i):
    check = 0
    b = False
    for j in range(len(line[i])):
        if line[i][j] == '(':
            check += 1
        elif line[i][j] == ')':
            check -= 1
        if check < 0:
            print("NO")
            b = True
            break
    if b is True:
        continue
    if check > 0:
        print("NO")
    else:
        print("YES")



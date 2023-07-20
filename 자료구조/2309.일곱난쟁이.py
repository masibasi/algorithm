from itertools import combinations

m = []
for _ in range(9):
    m.append(int(input()))

for c in combinations(m, 7):
    if sum(c) == 100:
        for i in sorted(c):
            print(i)
        break

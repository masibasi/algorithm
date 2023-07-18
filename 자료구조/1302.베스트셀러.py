# 이 문제는 딕셔너리를 얼마나 잘 아는지를 물어보는 문제였다.
# dict.values, dict.keys, dict.items 등 메소드등을 잘 알아야 한다. 생각보다 아주 쉽게 풀 수 있었다

N = int(input())
m = {}
for _ in range(N):
    book = input()
    if book in m:
        m[book] += 1
    else:
        m[book] = 1

max = max(m.values())
max_book = []

for k in m:
    if m[k] == max:
        max_book.append(k)

max_book.sort()
print(max_book[0])
import math

N, total = input().split(' ')
N = int(N)
total = int(total)
coins = []
for _ in range(int(N)):
    coins.append(int(input()))
count = 0

for i in range(int(N)):
    coin = coins[len(coins) - 1 - i]
    if coin <= total:
        divisor = math.floor(total / coin)
        count += divisor
        total -= (divisor * coin)
print(count)
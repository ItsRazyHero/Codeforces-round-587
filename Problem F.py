n, k = map(int, input().split())
scheme = list(map(int, input()))
 
prices = [0] * (n + 2)
scheme_r = [1000000000] * (n + 2)
 
for i in range(n, 0, -1):
    if scheme[i - 1] == 1:
        scheme_r[i] = i
    else:
        scheme_r[i] = scheme_r[i + 1]
 
for i in range(1, n + 1):
    prices[i] = prices[i - 1] + i
    idx = scheme_r[max(1, i - k)]
    if idx <= i + k:
        prices[i] = min(prices[i], prices[max(0, idx - k - 1)] + idx)
 
print(prices[n])

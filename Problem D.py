from math import gcd
from functools import reduce
 
def find_ppls(arr):
    max_a = max(arr)
    diffs = []
    for a in arr:
        diffs.append(max_a - a)
    z = reduce(gcd, diffs)
    y = 0
    for diff in diffs:
        y += int(diff / z)
 
    return f"{y} {z}"
 
num = int(input())
arr = [int(i) for i in input().split()]
print(find_ppls(arr))

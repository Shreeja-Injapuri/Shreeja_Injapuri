import sys
sys.setrecursionlimit(1000000000)
mod = 10000000007

def fibn(n):
    if n == 1:
        return 2
    if n ==2 :
        return 3

    a,b = 2,3
    for _ in range(n-2):
        a,b = b%mod,(a+b)%mod
    return b

testCases = int(input())
while testCases > 0 :
    n = int(input())
    print (fibn(n))
    testCases = testCases - 1

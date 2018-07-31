n = int(input())
theSum = 0
theArray = list(map(int, input().split()))
for num in theArray:
    theSum += num
    
print(theSum)

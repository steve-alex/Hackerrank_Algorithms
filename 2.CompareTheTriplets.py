a0,a1,a2 = input().strip().split(' ')
a = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b = [int(b0),int(b1),int(b2)]

Alice = 0
Bob = 0

for i in range(3):
    if a[i] > b[i]:
        Alice += 1
    elif a[i] < b[i]:
        Bob +=1
    else:
        pass

print(Alice, Bob)

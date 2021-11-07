M,N = map(int, input().split())

candy = []

for i in range(N):
    x = int(input())
    candy.append(x)

flag = True
while flag == True:
    for i in range(N):
        if candy[i] > 0:
            candy[i] -= 1
        M -= 1
        if M == 0:
            flag = False
            break
ans = 0
for i in range(len(candy)):
    ans = ans + candy[i]**2

print(ans%2**64)



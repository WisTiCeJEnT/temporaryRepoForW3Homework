import math
n = int(input())
inpl=[]
ans = 0
a = b = -1
for i in range (0,n):
    inpl.append(int(input()))
    if(inpl[len(inpl)-1]>8):
        print("error")
        exit()
while(inpl):
    ans += 1
    a = inpl.pop(0)
    if(inpl):
        if(math.fabs(a-inpl[0]) <= 1):
            b = inpl.pop(0)
            if(inpl):
                if(math.fabs(a-inpl[0])<=1 or math.fabs(b-inpl[0])<=1):
                    inpl.pop(0)
print(ans)

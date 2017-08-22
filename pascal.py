import math
def printpc(r):
    for i in range (0,r):
        c=0
        for j in range (0,r):
            if(r-i-1>j):
                print("",end=" ")
            else:
                print(cpr(i,c),end=" ")
                c+=1
        print()
def cpr(n,k):
    return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

n = int(input("Size : "))
if(n>=0 and n<=13):
    printpc(n)
else:
    print("ERROR")    

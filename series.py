def a(n):
    return 1+(n-1)*2
def b(n):
    if(n<=2):
        return 1
    return b(n-1)*(n-1)
def sum_a(n):
    return int((n/2.0)*(2+(n-1)*2))
def sum_b(n):
    if(n==0):
        return 0
    return sum_b(n-1)+b(n)

n = int(input())
print("a({}) = {}".format(n,a(n)))
print("b({}) = {}".format(n,b(n)))
print("sum_a({}) = {}".format(n,sum_a(n)))
print("sum_b({}) = {}".format(n,sum_b(n)))

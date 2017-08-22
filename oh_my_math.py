#1==============================================================
def my_ceiling(x):
    if(x>=int(x)):
        return int(x)+1
    else:
        return x
#2==============================================================
def my_floor(x):
    return int(x)
#3==============================================================
def my_fabs(x):
    if(x>0):
        return x
    return -1*x
#4==============================================================
def my_factorial(x):
    if(x==1):
        return 1
    else:
        return my_factorial(x-1)*x
#5==============================================================
def my_exp(x):
    return pow(my_e(),x)
#6==============================================================
def my_pow(x,y):
    ans=1
    for i in range (0,y):
        ans *= x
    return ans
#7==============================================================
def my_sqrt(x):
    y=x/10
    tmp = x
    i=0.01
    while(tmp>1):
        tmp/=10
        i*=10
    for l in range (0,40):
        while((y+i)*(y+i)<=x):
            oy=y
            y+=i
            if(oy==y):
                break
        i/=10
    return y
#8==============================================================
def my_cos(x):
    ans = 1.0
    for i in range (1,15):
        if(i%2==0):
            ans += my_pow(x,i*2)/my_factorial(i*2)
        else:
            ans -= my_pow(x,i*2)/my_factorial(i*2)
    return ans
#9==============================================================
def my_sin(x):
    ans = x
    for i in range (1,25):
        if(i%2==0):
            ans += my_pow(x,i*2+1)/my_factorial(i*2+1)
        else:
            ans -= my_pow(x,i*2+1)/my_factorial(i*2+1)
    return ans
#10==============================================================
def my_tan(x):
    return my_sin(x)/my_cos(x)
#11==============================================================
def my_degree(x):
    return (x%(2*my_pi())/my_pi()*180)
#12==============================================================
def my_radian(x):
    return (x%360)/180*my_pi()
#13==============================================================
def my_pi():
    return 3.141592653589793
"""    ans = 3 
#my_pi=3.141592653589787 math.pi=3.141592653589793
    for i in range(1,1000000):#For the best accuracy(0.000000000000006 miss) 
        j=i*2
        if(i%2==0):
            ans -= 4/((j)*(j+1)*(j+2))
        else:
            ans += 4/((j)*(j+1)*(j+2))
    return ans"""
#14==============================================================
def my_e():
    return 2.718281828459045 #2.7182818284590452353602874713527 :)
"""    n=10000000 #This is too slow and inaccuracy
    return my_pow(1+1/n,n)"""
#main============================================================
inp = float(input())
#print(my_sqrt(inp))
#print(my_degree(my_pi()))
#print(my_radian(180))

import math
def gcd(a,b):
    if(a%b==0):
        return b
    else:
        return gcd(b,a%b)
def print1ans(i):
    if(i%(2*a)==0):         #i int
        i=int(i/2/a)
        if(i>0):
            print(f"= {K}(x-{i})(x-{i})")
            print(f"= {K}(-x+{i})(-x+{i})")
        else:
            i = -i
            print(f"= {K}(x+{i})(x+{i})")
            print(f"= {K}(-x-{i})(-x-{i})")
    else:                   #i float
        tmp = 2*a
        G = gcd(i,tmp)
        if(G!=1):
            i  =  i//G
            tmp =  tmp//G
        if(i>0):
            print(f"= {K}({tmp}x-{i})({tmp}x-{i})")
            print(f"= {K}(-{tmp}x+{i})(-{tmp}x+{i})")
        else:
            i = -i
            print(f"= {K}({tmp}x+{i})({tmp}x+{i})")
            print(f"= {K}(-{tmp}x-{i})(-{tmp}x-{i})")
def printans(i1,i2):
    S11 = ""
    S12 = ""
    S21 = ""
    S22 = ""
    if(i1%(2*a)==0):        #i1 int
        i1=int(i1/2/a)
        if(i1>0):
            S11 = ("(x-{})".format(i1))
            S12 = ("(-x+{})".format(i1))
        else:
            S11 = ("(x+{})".format(-i1))
            S12 = ("(-x-{})".format(-i1))
    else:                   #i1 float
        tmp = 2*a
        G = gcd(i1,tmp)
        if(G!=1):
            i1  =  i1//G
            tmp =  tmp//G
        i1 = int(i1)
        if(i1>0):
            S11 = ("({}x-{})".format(tmp,i1))
            S12 = ("(-{}x+{})".format(tmp,i1))
        else:
            S11 = ("({}x+{})".format(tmp,-i1))
            S12 = ("(-{}x-{})".format(tmp,-i1))
#i2
    if(i2%(2*a)==0):        #i2 int
        i2 = int(i2/2/a)
        if(i2>0):
            S21 = ("(x-{})".format(i2))
            S22 = ("(-x+{})".format(i2))
        else:
            S21 = ("(x+{})".format(-i2))
            S22 = ("(-x-{})".format(-i2))
    else:                   #i2 float
        tmp = 2*a
        G = gcd(i2,tmp)
        if(G!=1):
            i2  =  i2//G
            tmp =  tmp//G
        i2 = int(i2)
        if(i2>0):
            S21 = ("({}x-{})".format(tmp,i2))
            S22 = ("(-{}x+{})".format(tmp,i2))
        else:
            S21 = ("({}x+{})".format(tmp,-i2))
            S22 = ("(-{}x-{})".format(tmp,-i2))
    if(a>0):
        print("= "+K+S11+S21)
        print("= "+K+S21+S11)
        print("= "+K+S12+S22)
        print("= "+K+S22+S12)
    else:
        print("= "+K+S12+S21)
        print("= "+K+S21+S12)
        print("= "+K+S11+S22)
        print("= "+K+S22+S11)
        
#Main======================================================    
print(u"Standard form is Ax**2+Bx+C")
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
A = str(a)
B = str(b)
K = ""
if(gcd(a,gcd(b,c))!=1):
    K = "("+str(gcd(a,gcd(b,c)))+")"
if(a==1):#for prevent 1x ... just x is ok.
    A = ""
if(b==1):
    B = ""
if(a==-1):
    A = "-"
if(b==-1):
    B = "-"
print("{}x**2+{}x+{}".format(A,B,c))
if((b*b)-4*a*c>0):
    x1 = int(-b+math.sqrt((b*b)-(4*a*c)))
    x2 = int(-b-math.sqrt((b*b)-(4*a*c)))
    printans(x1,x2)
elif((b*b)-4*a*c==0):
    print1ans(-b)
else:
    print("can't find factor by this pattern")

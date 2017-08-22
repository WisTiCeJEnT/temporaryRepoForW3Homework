def gcd(a,b):
    if(a%b==0):
        return b
    else:
        return gcd(b,a%b)
p = int(input())
q = int(input())
print(gcd(p,q))
#1 I think return the value back is better.Because it can in other purpose in other function
#2 For prevent a variable confusing because in Python it defined the variable in main as a global
#3 10,20,10
#4 First is in line 5 have an error because "x" in "input(x)" is not defined.... back to work is answer is 10,20,10 because f(x) pass value of x not an address or reference of x also in f(x) it defined a new x as an local variable.
#5 Same as in #4 pass by value is how we call a function and give it some value of veriable not an address or reference of it.

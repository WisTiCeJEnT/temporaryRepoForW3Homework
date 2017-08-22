t = int(input())
d = t//5 * 6.0
t = t%5
if(t>=3):
    t=3
if(t>0):
    d += (27*t-((t**4)/4))/10-0.075
print("{}".format(d))

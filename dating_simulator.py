def gin(S):
    inp = input(S)
    if(inp=="Y"):
        return True
    else:
        return False
def metS():
    return gin("Run into Stella ?: ")
E=0
Rem=0
S=0
Ro=0
while(1):
    if(gin("Dating with Emilia ?: ")):
        if(metS()):
            E+=1
        continue
    if(gin("Dating with Rem ?: ")):
        if(metS()):
            Rem+=1
        continue
    if(gin("Dating with Stella ?: ")):
        S+=1
        continue
    if(gin("Dating with Roswaal ?: ")):
        Ro+=1
    break
print("Subaru: {}\nEmilia: {}\nRem: {}\nStella: {}\nRoswaal: {}".format(E+Rem+S+Ro,E,Rem,S,Ro))

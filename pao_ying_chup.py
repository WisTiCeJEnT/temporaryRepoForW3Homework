def check_input(inp):#For checking user input
    listt = {"rock","scissors","paper"}
    if(inp in listt):
        return True
    return False
def getCon(StrInp):#For convert "yes/no" in "continue another game" to "T/F"
    if(StrInp=="yes"):
        return True
    else:
        return False
def pyc(inp1,inp2):#
    ruleList = {"rock":"scissors","scissors":"paper","paper":"rock"}
    if(inp1==inp2):
        print("It's a tie!!\nPlease continue")
        return False
    else:
        if(ruleList[inp1]==inp2):
            print(f"{P1} wins.")
        else:
            print(f"{P2} wins.")
        return True
#Main
P1 = input("Player 1 name : ")
P2 = input("Player 2 name : ")
print("Please input (rock/scissors/paper)")
contin = True
while(contin):
    in1 = input(f"{P1} : ")
    in2 = input(f"{P2} : ")
    if(check_input(in1) and check_input(in2)):
        if(pyc(in1,in2)):
            contin = getCon(input("Do you want to play another game (yes/no) : "))
    else:
        print("Invalid input\nPlease try again!!!")

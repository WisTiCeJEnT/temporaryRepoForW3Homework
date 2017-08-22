inp = float(input("Input distance (m) : "))
while(inp != 0):
    if(inp>10):
        print("You : I need healing!!!\nYou do not have internet signal [{:d} m]".format(int(inp)))
    elif(inp>2):
        print("You have 25% internet signal [In 2 - 10 : {:.2f} m]".format(inp))
    elif(inp>1):
        print("You have 50% internet signal [In 1 - 2 : {:.5f} m]".format(inp))
    else:
        print("You have 75% internet signal [In 0 - 1 : {:.5f} m]".format(inp))
    inp = float(input("Input distance (m) : "))
print("You have 100% internet signal [0.0 m]\nYou : GG Ez kid")

#exercise 1

def calc():
    keep_going = True
    while keep_going == True:
        num_1 = input("First number please!")
        num_2 = input("Second number please!")
        oper = input("+, -, *, or /?")
        if oper == "+":
            print(int(num_1) + int(num_2))
        elif oper == "-":
            print(int(num_1) - int(num_2))
        elif oper == "*":
            print(int(num_1) * int(num_2))
        elif oper == "/":
            print(int(num_1) / int(num_2))
        else:
            print("Please try again!")
        flagg = input("Would you like to go again? Y or N")
        if flagg.upper() == "N":
            keep_going = False
            
        else:
            continue

#Second exercise


def pyramid(n):
    
    x = "x"
    rows = 0
    i = n + 1

    while rows < n:
        print(space(i) + x)
        x = x + "xx"
        rows +=1
        i = i - 1
        
    

def space(n):
    i = 0
    space = " "
    while i < n-1:
        i+=1
        space = space + " " 
    return space     

print(pyramid(8))

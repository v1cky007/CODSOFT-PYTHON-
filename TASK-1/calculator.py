num1=int(input("Enter the number "))
num2=int(input("Eneter the number"))



while True:
    print("-------------------MENU---------------------")
    print(" ")
    print(" ")
    print("ENTER YOUR CHOICE")
    print("1.ADDITION")
    print("2.SUBTRACTION")
    print("3.MULPTIPLICATION")
    print("4.DIVISION")
    choice=int(input("Enter the choice:-"))
    if(choice==1):
        addans=num1+num2
        print("THE ADDITION OF NUMBER 1 AND NUMBER 2:-",addans)
    elif(choice==2):
        subans=num1-num2
        print("THE SUBTRACTION OF NUMBER 1 AND NUMBER 2:-",subans)
    elif(choice==3):
        mulans=(num1*num2)
        print("THE MULPTIPLICATION OF NUMBER 1 AND NUMBER 2:-",mulans)
    elif(choice==4):
        divans=(num1/num2)
        print("THE DIVISION OF NUMBER 1 AND NUMBER 2:-",divans)
    else:
        print("INVALID CHOICE")
        break

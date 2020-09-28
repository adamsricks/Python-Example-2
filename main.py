import number_class as num
Number = num.Number

def printOptions():
    print("Would you like to:")
    print("Add a number? (+)")
    print("Subtract a number? (-)")
    print("Multiply a number? (*)")
    print("Divide by a number? (/)")
    print("Clear the current number? (c)")
    print("Quit the calculator? (q)")

def main():
    yourNum = None
    calAgain = True
    ansAgain = True
    playAgain = ""
    answer = ""
    print("Welcome to the mini-calculator!")    
    
    while calAgain == True:
        actingNum = 0
        ansAgain = True
        playAgain = ""

        if yourNum == None:
            print()
            yourNum = Number(input("Enter a number: "))

        print()
        print(str(yourNum))
        print()
        printOptions()

        while ansAgain == True:
            answer = input("")
            if answer == "c":
                yourNum = None
                ansAgain = False
            elif answer == "+":
                actingNum = input("Enter a number to add by: ")
                yourNum.add(actingNum)
                ansAgain = False
            elif answer == "-":
                actingNum = input("Enter a number to subtract by: ")
                yourNum.sub(actingNum)
                ansAgain = False
            elif answer == "*":
                actingNum = input("Enter a number to multiply by: ")
                yourNum.mult(actingNum)
                ansAgain = False
            elif answer == "/":
                actingNum = input("Enter a number to divide by: ")
                yourNum.div(actingNum)
                ansAgain = False
            elif answer == "q":
                ansAgain = False
                calAgain = False
            else:
                print("Please enter a valid symbol (+,-,*,/,n).")
        


if __name__ == "__main__":
    main()
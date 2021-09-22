# print("Hello World")
# print("What is your name?")
# myName = input()
# print("It is good to meet you", myName)
# print("The length of your name is:", len(myName))
# print("What is your age?")
# myAge = input()
# print("you will be" + str(int(myAge) +5) + "in 5 years")
print("Title: Area of Trapezoid Calculator")
print("""/---------\\
        /          \\
       /            \\              
      /--------------\\""")
firstBase = int(input("What is the first base of the trapezoid?"))
secondBase = int(input("What is the second base of the trapezoid?"))
myHeight = int(input("What is the height of the trapezid?"))
areaformula = float ((firstBase + secondBase)/2) * myHeight
print(f"The Area of the trapezoid is", areaformula)

def areaformula(firstBase, secondBase, myHeight):
    print(f"Area of Trapezoid is {(int(firstBase)) + (int(secondBase)) * 0.5 * int(myHeight)}")
print("firstBase is 2")
print("secondBase is 4")
print("myHeight is 8")
areaformula(2, 4, 8)
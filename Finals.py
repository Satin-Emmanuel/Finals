def act_1(a):
    print(f"Hello World")
def act_2():
    name = input ("Eman")
    
    print("hi" + name )
def act_3():
    name = input("Please input your name here ---> ")
    fname = input("Please input your fname here ---> ")
    mname = input("Please input your mname here ---> ")
    birthdate = input("Please input your birth date here ---> ")
    birthmonth = input("Please input your birthmonth here ---> ")
    birthyear = input("Please input your birthyear here ---> ")
    maritalstatus = input("Please input your maritalstatus here ---> ")
    religion = input("Please input your religion here ---> ")
    ethnicity = input("Please input your ethnicity here ---> ")
    mobile = input("Please input your mobile here ---> ")
    email = input("Please input your email here ---> ")
    gender = input("Please input your gender here ---> ")
    address = input("Please input your address here ---> ")
    age = input(" Please input your age here ---> ")


    print("\n\n\n\n\tHello, My name is,", name ,"I'm", age ,"yrs old.\n\tI identify as", gender ,"\n\tMy father's name is", fname ,"\n\tMy mother's name is", mname ,"\n\tMy Bithday is in", birthmonth , birthdate , birthyear ,"\n\tI live in", address,"\n\tI am", maritalstatus ,"\n\tI am", ethnicity ,"Citizen\n\tMy mobile number is:", mobile ,"\n\tYou may contact me in my email:", email ,"\n\tThank You!!!\n\n\n")

def act_4():
    number1 = eval(input("please type number--->"))
    number2 = eval(input("please type number--->"))

    answer	= number1 + number2
    print ("the sum of", number1, "and" , number2, "is" ,answer)
def act_5():
    print('\n\t\t\t\t\t\t=================================')
print('\t\t\t\t\t\t|FAHRENHEIT TO CELSIUS CONVERTER|')
print('\t\t\t\t\t\t=================================')
temp=eval(input('\nEnter Temperature in Fahrenheit: '))
celsius=(temp - 32) * 5/9
print(f'\n\nThe conversion of {temp} degrees Fahrenheit is {celsius} degrees Celsius\n\nor')
print(f'\nThe conversion of {temp} degrees Fahrenheit is {round(celsius, 2)} degrees Celsius')
def act_6():
    x = 5

    print (x)

    x = x + 10

    print (x)

    x = x + 15

    print(x)

    x += 10

    print(x)
    
def act_7():
    gold = 0

    miner = input("Enter Name")

    hasmine = input("Did you mine gold today ?")

    if hasmine.lower() == "yes":
        gold +=1
        print (f"Hi {miner}, today you have a total of {gold} gold ")
    else: 
        print (f"Hi {miner}, today you have a total of {gold} gold ")
        
def act_8():
    password = input("please enter your password : ")

    if password.lower() == " mahal ko pa sya ":
        print (" congrats ang rupok mo")
        print ("enjoy using the system")
    elif password == "mahal ko pa sya":
        print (" congrats ang rupok mo")
        print ("enjoy using the system")


    else:
        print ("bawal ang marupok")
    print ("thank you for using the system")
def act_9():
    age = eval(input(" enter your age : "))
    if age>= 1 and age <= 7 :
        print ("toddler")
    elif age >= 8 and age <= 13:
        print (" pre teen")
    elif age >= 14 and age <= 18:
        print("Teenager")
    elif age <= 21:
        print("Early Adulthood")
    elif age <= 45:
        print("Mid Adulthood")
    elif age <= 59:
        print("Post Adult")
    elif age >= 60 and age <= 100:
        print("Senior")
    else:
        print("INVALID AGE")
def act_10():
    isDLL= input('Are you a current student of DLL (yes/no):  ')

    if isDLL.lower() == 'yes':
        print('Welcome to the DLL BSIT Scholarship form')
        isCotta= input('Are you from Barangay Mayao silangan (yes/ no):  ')

        if isCotta.lower() == 'yes':
            print('Please fillup the second form')
            isLevel=input('What is your current level right now in DLL\nF - Freshmen\nS - Sophomore\nJ - Junior\nR - Senior\nPlease input your answer')
            if isLevel.lower() == 'f':
                print('Hi Freshmen')
            elif isLevel.lower() == 's':
                print('Hi Sophomore')
            elif isLevel.lower() == 'j':
                print('Hi Junior')
            elif isLevel.lower() == 'r':
                print('Hi Senior')
            else:
                print('Invalid choice')
            isNeeded = input('Do you need this scholarship (yes/no):  ')
        
            if isNeeded.lower() == 'yes':
                print('Scholarship Granted')
            else:
                print('Thanks for stopping by')
        else:
            print('Sorry, this Scholarship grant are only for resident of Mayao silangan')

    else:
        print('Thanks for stopping by')
def act_11():
    for ako in range (1 , 101):
        print(ako, 'Byee gar!')
def act_12():
    for cyclone in range (10,0,-1):
        print(cyclone)
def act_13():
    sum = 1
num=int(input('Enter a number: '))
for x in range (num,0,-1):
    sum *= x
print(f"The factorial of {num} is {sum}")
def act_14():
    for y in range ( 0, 11,):
        print(y,end =" ")
    for a in range (0, 11):
        print("*",end = " ")
    print("")
def act_15():
    for a in range ( 0, 11,):
        print(a,end =" ")
    for y in range (0, a):
        print("*",end = " ")
    print("")
def act_16():
    for a in range (1,11,):
     for b in range (1, a + 1):
        print(" ",end=" ")
    for c in range(11, a, -1):
        print(" * ",end=" ")
    print()
def act_17():
    col = eval(input("Enter number of columns---> "))


    for x in range (1, 11):
        for y in range (1, col + 1):
            print(f"{x} x {y} = {x*y}" ,end="\t")
        print()
def act_18():
    tri = eval(input("Enter a number of triangle---> "))

    for a in range (1, 6):
        for r in range (1 , tri + 1):
            for y in range (1 , a + 1):
                print("*", end=" ")
            for z in range (6, x, -1):
                print(" ",end=" ")
def act_19():
    tuloy = True
    while tuloy == True:
        name = input("Enter your name: ")
        if name.lower()== "stop":
            print("PROGRAM TERMINATED")
            break
            tuloy = False
        else:
            continue
def act_20():
    import os

    isContinue = True
    no = 0
    while isContinue == True:
        ask = input("Would you like to add another triangle (yes / no )--> ")

        if ask.lower() == "no":
            print("PROGRAM TERMINATED")
            break
            isContinue = False
        else:
            os.system('cls')
            no += 1
            for a in range (1, 6):
                for r in range (1 , no + 1):
                    for y in range (1 , a + 1):
                        print("*", end=" ")
                    for z in range (6, a, -1):
                        print(" ",end=" ")
                print()
            continue
def act_21():
    def pang_bati():
        print("HI IT1C")

def pang_bati_v2(name):
    print(f"Hello {name}")

def termi():
    print("PROGRAM TERMINATED")

def activity_2():
    number1 = eval (input("enter a number--->" ))
    number2 = eval (input("enter another number--->" ))
    answer = (number1 + number2)
    print(f"The sum of {number1} and {number2} is {answer}")

tuloy =  True
while tuloy == True:
    ask = input("Enter a name---> ")

    if ask.lower() != "stop":
        pang_bati_v2(ask)
        if ask == "2":
            activity_2()
            continue
    else:
        termi()
        break
def act_22():
    def act_22():  
    
        def act_1():
            print("Hello World")
    act_1()
    act_22()
def act_23():
    def factorial(number):
        """ This function's purpose is to compute/calculate the factorial of any number given """
        fact = 1
        for x in range(number, 0, -1):
             fact *= x

        return fact

    print(f"the factorial of 10 is {factorial(10)}")
def act_24():
    from activity23 import factorial

    print(f"the factorial of 8 is {factorial(8)} ")
def act_25():
    courses = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]

    courses.remove("Delete w/o index")
    courses.pop()
    courses.append("DHRS")
    courses.insert(0, "ABELS")

    print(courses)
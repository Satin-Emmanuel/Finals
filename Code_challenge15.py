import os
e = 1
loop = True

while loop == True:
    tc = input("Would you like to add a triangle? (yes / no)> ")
    if tc.lower() == "yes":
        os.system("cls")
        e += 1
        for x in range(1, 6):
            for n in range(1, e):
                for y in range(1, x +1):
                    print("*", end=" ")
                for h in range(6, x, -1):
                    print(" ", end=" ")
            print()
    elif tc.lower() == "no":
        os.system("cls")
        print("Program shutdowned.")
        break
        loop = False
    else:
        print("Invalid input please use only yes or no.")
        continue
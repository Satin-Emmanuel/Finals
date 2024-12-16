isLoop = True
number = 0

while isLoop == True:
    isho = eval(input("Enter a number--> "))
    if isho > 0:
        number += isho
        continue
    elif isho == 0:
        print("Loop has been shutdowned.")
        print(f"the sum of all the numbers given is {number}")
        break
        isLoop = False
    else:
        print("Please enter a number.")
        continue
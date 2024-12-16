tri = eval(input("Enter a number of triangle---> "))
for a in range (1, 6):
    for b in range (1 , tri + 1):
        for c in range (1 , a + 1):
            print("*", end=" ")
        for d in range (6, a, -1):
            print(" ",end=" ")
    print()
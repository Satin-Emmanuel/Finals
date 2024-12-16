col = eval(input("Enter number of columns---> "))
for a in range (1, 11):
    for y in range (1, col + 1):
        print(f"{a} x {y} = {a*y}" ,end="\t")
    print()
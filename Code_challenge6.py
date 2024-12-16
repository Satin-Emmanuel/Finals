prelim = eval(input("Enter your grade for prelims: "))
mid = eval(input("Enter your grade for midterms: "))
semis = eval(input("Enter your grade for semis: "))
finals = eval(input("Enter your grade for finals: "))
quiz = eval(input("Enter yuor grade for quiz: "))
proj = eval(input("Enter your grade for project "))


if(prelim >= 65 and prelim <=100) and (mid >= 65 and mid <=100) and (semis >= 65 and semis <=100) and (finals >= 65 and semis <=100) and (quiz >=65 and quiz <=100) and (proj >=64 and proj <=100):
	FG =(prelim * .15) + (mid * .15) + (semis * .15) + (finals * .15) + (quiz * .25) + (proj * .15)


if FG > 100:
	print("You exceeded the expectations")


elif FG >= 75:
	print(f"your grade is {FG}")
	print("Congrats you passed")



else:
	print(f"Your grade is {FG}")
	print("Sorry better luck next time")
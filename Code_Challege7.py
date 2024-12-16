A = input("DID YOU BUY A GOOD/s (yes/no)? ")
B = input("\nName of the  goods: ")
price = float(input("Price of the  goods: "))
age = int(input("What is your age: "))
E = float(input("Amount Given: "))

if age >= 60:
		F = price * 0.123  
		G = price + F 
		I = G * 0.052 
		J = G - I
		H = E - J  
		print("Hi, customer, you purhased a ",B,"with a price of ",price," plus a 12.3% tax( ",F,") and with a discount of",I)
		print("total of PHP ",J)
		print("Amount Given: ",E)
		print("change: PHP",H)
		print("\nThank you for your purchase, customer!")
else:
		F = price * 0.123 
		G = price + F 
		H = E - G   
		print("Hi, customer, you purhased a ",B,"with a price of ",price," plus a 12.3% tax( ",F,")")
		print("total of PHP ",G)
		print("Amount Given: ",E)
		print("change: PHP",H)
		print("Thank you for your purchase!")
  
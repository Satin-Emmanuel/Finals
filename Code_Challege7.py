A = input("DID YOU BUY A MEAT GOOD/s (yes/no)? ")
if A.upper() == "YES":
	print('\nTHIS ARE THE LIST OF AVAILABLE MEAT GOODS')
	print('===========================================')
	print('Pork ------- 300php/kilo')
	print('Chicken ---- 250php/kilo')
	print('Beef ------- 400php/kilo')
	print('Rabbit ----- 250php/kilo')
	print('Tocino ----- 100php/kilo')
	print('Bacon ------ 120php/kilo')
	print('Bologna -----100php/kilo')
	quan1= eval(input("\nHow many kilos of Pork meat you want to buy? "))
	pork=quan1 * 300
	quan2= eval(input("\nHow many kilos of Chicken meat you want to buy? "))
	chicken=quan2 * 250
	quan3= eval(input("\nHow many kilos of Beef meat you want to buy? "))
	beef=quan3 * 400
	quan4= eval(input("\nHow many kilos of Rabbit meat you want to buy? "))
	rabbit=quan4 * 250
	quan5= eval(input("\nHow many kilos of Tocino meat you want to buy? "))
	tocino=quan5 * 100
	quan6= eval(input("\nHow many kilos of Bacon meat you want to buy? "))
	bacon=quan6 * 120
	quan7= eval(input("\nHow many kilos of Bologna meat you want to buy? "))
	bologna=quan7 * 100
	total= pork+chicken+beef+rabbit+tocino+bacon+bologna
	tax=(pork*0.123) or (chicken*0.123) or (beef*0.123) or (rabbit*0.123) or (tocino*0.123) or (bacon*0.123) or (bologna*0.123)
	total_and_tax= (total + tax)
	print()
	age = input("Are you a Senior Citizen(yes/no)? ")
	if age.lower() =='yes':
		disc=round(total*0.052)
		print(f"Hi, customer, you purhased a \n{quan1}kilo of Pork meat\n{quan2}kilo of Chicken meat\n{quan3}kilo of Beef meat\n{quan4}kilo of Rabbit meat\n{quan5}kilo of Tocino meat\n{quan6}kilo of Bacon meat\n{quan7}kilo of Bologna meat\nwith the total price of {total}php plus a 12.3% tax ({tax}php) and with a discount of 5.2% ({disc}php)")
	
	else:
		disc=0
		print(f"Hi, customer, you purhased a \n{quan1}kilo of Pork meat\n{quan2}kilo of Chicken meat\n{quan3}kilo of Beef meat\n{quan4}kilo of Rabbit meat\n{quan5}kilo of Tocino meat\n{quan6}kilo of Bacon meat\n{quan7}kilo of Bologna meat with the total price of {total}php plus a 12.3% tax(",tax,")")
	print()
	E = float(input("Amount Given: "))
	print()
	if E>= total_and_tax:
		change = round(E - total_and_tax + disc)
		print('=================RECEIPT===================')
		print('Qty.    Description           Amount')
		print(f'{quan1}x ----- PORK MEAT.........{pork}php')
		print(f'{quan2}x ----- CHICKEN MEAT......{chicken}php')
		print(f'{quan3}x ----- BEEF MEAT.........{beef}php ')
		print(f'{quan4}x ----- RABBIT MEAT.......{rabbit}php')
		print(f'{quan5}x ----- TOCINO MEAT.......{tocino}php')
		print(f'{quan6}x ----- BACON MEAT........{bacon}php')
		print(f'{quan7}x ----- BOLOGNA MEAT......{bologna}php')
		print()
		print(f'SUBTOTAL...................{total}php')
		print(f'TAX(12.3%).................{tax}php')
		print(f'TOTAL......................{total_and_tax}php')
		print(f'PAY AMOUNT.................{E}php')
		print(f'DISCOUNT(5.2%).............{disc}php') 
		print(f'CHANGE.....................{change}php')
		print()
		print("==THANK YOU COME AGAIN!!==")
	else:
		E< total_and_tax
		print("Insufficient Amount")
else :
	print("Thankyou for stopping by!")
  
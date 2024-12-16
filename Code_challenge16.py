def denomination(currency):
    print("\nDenomination Breakdown:")
    A = currency // 1000
    AA = currency % 1000

    B = AA // 500
    BB = AA % 500

    C = BB // 200
    CC = BB % 200

    D = CC // 100
    DD = CC % 100

    E = DD // 50
    EE = DD % 50

    F = EE // 20
    FF = EE % 20

    G = FF // 10
    GG = FF % 10

    H = GG // 5
    HH = GG % 5

    I = HH // 1

    print("1000---", A)
    print("500----", B)
    print("200----", C)
    print("100----", D)
    print("50-----", E)
    print("20-----", F)
    print("10-----", G)
    print("5------", H)
    print("1------", I)


accounts = {}

def create_account():
    username = input("Enter a username: ")
    if username in accounts:
        print("Account already exists!")
    else:
        accounts[username] = 0
        print(f"Account created successfully for {username}.")


def deposit():
    username = input("Enter your username: ")
    if username in accounts:
        try:
            amount = int(input("Enter amount to deposit : "))
            if amount > 0:
                accounts[username] += amount
                print(f"Deposited {amount} successfully. New balance: {accounts[username]}")
                denomination(amount)
            else:
                print("Amount must be positive!")
        except ValueError:
            print("Invalid input! Please enter a whole number.")
    else:
        print("Account not found!")


def withdrawal():
    username = input("Enter your username: ")
    if username in accounts:
        try:
            amount = int(input("Enter amount to withdraw (whole numbers only): "))
            if 0 < amount <= accounts[username]:
                accounts[username] -= amount
                print(f"Withdrawn {amount} successfully. Remaining balance: {accounts[username]}")
                denomination(amount)
            else:
                print("Insufficient funds or invalid amount!")
        except ValueError:
            print("Invalid input! Please enter a whole number.")
    else:
        print("Account not found!")


def check_balance():
    username = input("Enter your username: ")
    if username in accounts:
        print(f"Your balance: {accounts[username]}")
    else:
        print("Account not found!")


def options():
    while True:
        print("\nBanking System")
        print("C. Create Account")
        print("D. Deposit")
        print("W. Withdraw")
        print("CB. Check Balance")
        print("E. Exit")
        choice = input("Choose an setting (C-E): ")

        if choice == 'C':
            create_account()
        elif choice == 'D':
            deposit()
        elif choice == 'W':
            withdrawal()
        elif choice == 'CB':
            check_balance()
        elif choice == 'E' or "Exit":
            print("Thank you for choosing this Banking System!")
            break
        else:
            print("Invalid setting. Please try again.")

options()
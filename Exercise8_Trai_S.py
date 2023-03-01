username = input("Username : ")
password = input("Password : ")
A1 = 0
B2 = 0
if username == "client" and password == "1234":

    print("Login successful")
    print("Welcome to Grocer's store")
    print("-------------------------")
    print("Product list        price")
    print("1.Apple               1$")
    print("2.Banana              1.5$")

    choose = int(input("What do you want? : "))
    if choose == 1 :
        A1 = int(input("How many apples do you want? : "))

        more = input("Do you want any things else?>>Yes(Y) or No(N) : ")
        if more == "Y":
            choose = int(input("What do you want? : "))
            if choose == 1 :
                A1 = int(input("How many apples do you want? : "))
            elif choose == 2:
                B2 = int(input("How many bananas do you want? : "))

    elif choose == 2 :
        B2 = int(input("How many bananas do you want? : "))

        more = input("Do you want any things else?>>Yes(Y) or No(N) : ")
        if more == "Y":
            choose = int(input("What do you want? : "))
            if choose == 1:
                A1 = int(input("How many apples do you want? : "))
            elif choose == 2:
                B2 = int(input("How many bananas do you want? : "))

    else :
        more = input("Do you want any things else?>>Yes(Y) or No(N) : ")
        if more == "Y":
            choose = int(input("What do you want? : "))
            if choose == 1 :
                A1 = int(input("How many apples do you want? : "))
            elif choose == 2 :
                B2 = int(input("How many bananas do you want? : "))

    print("Summary")
    print("-------------------------")
    if A1 > 0:
        print("Apple(1$)", "*", A1, ">>", A1 * 1, "$")

    if B2 > 0:
        print("Banana(1.5$)", "*", B2, ">>", B2 * 1.5, "$")

    print("Total >>", ((A1 * 1) + (B2 * 2)), "$")
    print("-------------------------")
    print("Thank you for coming")

else :
    print("Username or Password was wrong")
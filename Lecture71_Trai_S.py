menuList = []
priceList = []
totalprice = 0
def showBill():
    print("----- My menu -----")
    for i in range(len(menuList)):
        print(menuList[i], priceList[i])
    print("Total :", totalprice)

while True:
    menuName = input("Please Enter Menu : ").lower()
    if(menuName == "exit"):
        break
    else:
        menuPrice = input("price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
        totalprice += int(menuPrice)
print(menuList, priceList)

showBill()



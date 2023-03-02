p = int(input("How many levels of pyramid : "))
x = ""
y = ""
for i in range(p):
    x = "*"*(i+1+i)
    y = " "*(p-(i+1))
    print(y+x)

print("enter three no. to which is greater")
a=int(input("ente first no.: "))
b=int(input("enter second no.: "))
c=int(input("enter third no.: "))
if a>=b :
    if a>=c :
        print("greater no. is",a)
    else :
        print("greater no. is",b)
else :
    if b>=c :
        print("greater no. is",b)
    else :
        print("greater no. is",c)
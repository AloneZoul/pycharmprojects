
size=int(input("Enter The Size Of THe Pyramid"))
i=1

while i<=size:
    j=size-1
    while j>=i:
        print(" ",end="")
        j=j-1
    k=1
    while k<=i:
        print("* ",end="")
        k=k+1
    print()
    i=i+1



n = int(input("Enter rows: "))

i = 1


while i <= n:
    j=1
    while j<=i:
      print(i,end="")
      j+=1
    k=1
    while k<=n-i:
         print(" ",end="")
         k+=1
    print()

    i+=1
        

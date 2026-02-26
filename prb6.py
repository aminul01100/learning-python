num = int(input("Enter number: "))
originalNum = num
reverse = 0
while num>0:
    i = num%10
    reverse = reverse*10 + i
    num = num//10

print("Original number: ",originalNum)
print("Reversed number: ",reverse)

    

    
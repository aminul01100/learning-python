num = int(input("Enter number: "))
digits = str(num)
sum = 0
for (digit) in digits:
    digit = int(digit)
    if (digit)%2 == 1:
       print(digit,"^3 =  ",digit**3)
       sum = sum + (digit**3)
    else:
        continue
sum = str(sum)
print("Sum of cubes = ",sum)
if sum == digits:
    
    print(sum," is a Modified Armstrong Number")



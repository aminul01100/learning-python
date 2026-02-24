num = int(input("Enter number: "))
main = num
if num>0:
    factorial = []
    Multi = 1
    while num>=1:

        factorial.append(str(num))
        Multi = Multi *num
        num -=1 
  
    print(main,"! ="," × ".join(factorial)," = ",Multi) 
else:
    print("Error")       
num = int(input("Enter number: "))

digits = list(str(num))

print("Digits:",",".join(digits))

nonZero=[]

count = 0
for d in digits:
    if d == "0":
        continue
    else:
        count += 1
        nonZero.append(d) 
print("Non-zero digits: ",",".join(nonZero))  
print("Number of Non-zero digits: ",count)  
print("Zeros were skipped using continue!")  


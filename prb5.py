num = int(input("Enter number: "))
allDigit = list(str(num))

odd = []
even = []
sum =0
print("All digits: ",",".join(allDigit))
for (digit) in allDigit:
    if int(digit)%2 == 0:
        even.append(digit)
        continue
    else:
        odd.append(digit)
        sum+=int(digit)
print("Odd digits: ",",".join(odd))
print("Even digits (",",".join(even),") were skipped using continue")
print("Sum of odd digits = ",sum)


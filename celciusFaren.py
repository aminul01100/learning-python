num = int(input("Choice (1 for C to F, 2 for F to C)"))
temp = int(input("Enter temperature:"))
if num ==1:
    F = round((temp * 9/5) + 32)
    print(temp,"°C = ",F,"°F")
elif num==2:
     C =round ((temp - 32) * 5/9)
     print(temp,"°F = ",C,"°C")




year = int(input("Enter number: "))

if year%4 ==0 and year%100!=0:
    print(year ,"is a leap year")
    print("February ",year," has 29 days")
elif year%400 ==0:
    print(year ,"is a leap year")
    print("February ",year," has 29 days")
else:
    print("This is not a leap year")    
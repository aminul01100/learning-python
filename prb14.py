validNum = []
skipNum= []
sum = 0
while True:
    num = int(input("Enter number: "))

    if num < 0 or num > 100:
        skipNum.append(num)
        continue
    elif  num == 0 :
        break
    else:
        print(num)
        sum = sum + num
        validNum.append(num)

lenth = len(validNum)
avge = sum/lenth
print("Valid numbers: ",str(validNum))
print("sum :", sum,"| Average:",avge ,"| Count :",lenth)
print(type(validNum))

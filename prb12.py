count =0
while True:
    num = int(input("Question 1: 3 × 4 = ? → " ))
    if num != 12:
        break
    else:
        print("Question 1: 3 × 4 = ? → 12  Correct!")
        count+=1
        num2 = int(input("Question 2: 5 × 3 = ? → ")) 
        if num2 != 15:
         break
        else:
         print("Question 2: 5 × 3 = ? → 15  Correct!")
         count+=1
         break
    
print("Perfect score! You got all ",count," correct!")    
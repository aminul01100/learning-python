str = (input("Enter text: "))
originalStr =str
count = 0
skipCount =0
vowel =[]
consonant = []
print("Original text: ",originalStr)

for char in str:
    if char =="a"or char=="e"or char=="i"or char=="o"or char=="u":
        count += 1
        print(char," (vowel) - counted")
        vowel.append(char)

    else:
        print(char," (consonant) - skipped")
        skipCount += 1
        consonant.append(char)
        continue
print("Vowels found:",vowel)
print("Total vowels: ",count)
print("Characters skipped (using continue): ",skipCount)


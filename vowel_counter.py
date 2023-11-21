def vowel_count():
    word = input("Enter the string : ")
    word = word.lower()
    word = word.replace(" ","") 
    vowel = 'aeiou'
    count = 0
    for item in word:
        if item in vowel:
            count = count + 1
    print("The number of vowels = ", count)


vowel_count()
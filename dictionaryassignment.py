# Question a)
#The code runs throught the sentence and if the word is in the sentence it adds one to its value and if it isnt it gets added to the
#dictionary and is assigned the value 1

sentence = input("Enter a sentence: ")
chars = {}
#for char in sentence:
    #chars[char] = chars.get(char, 0) + 1
    #print(char)
    #if char in chars:
     #   chars[char] = chars[char] + 1
    #else:
     #   chars[char] = 1
#print(chars)

#Question b)
#print(char) will print each character in the sentence one by one but without it you just get the output of the dictionary

#Question c)
#Dictionary

#Question d)
#The chars keys are the letters in the sentence and the value is how many times they appear

#Question e)
#It behaves the same as the original code and counts the amount of times each letter appears in the sentence

#Question a)
#.get is searching for the value of the char in the dictionary and adding one to its value if it exists and giving it a value of 0
#if it doesnt exist

#Question g)
'''
vowels = ["a","e","i","o","u"]
vowel = 0
consonants = 0
#for char in vowels:
for char2 in sentence:
        if char2 in vowels:
        #if char== char2:
            chars[char2] = chars.get(char2, 0) + 1
        else:
            chars[char2] = chars.get(char2, 0) +1

print(chars)
for chars3 in sentence:
    if chars3 in vowels:
        vowel = vowel+1
    else:
        consonants = consonants + 1
    
print(vowel)
print(consonants)
'''
words = {""}
join = []
abc=""
cba = ""
for letter in sentence:
    abc= abc+letter
    if letter == " ":
        cba = abc
        join.append(abc)
        abc = abc-cba
'''
for word in sentence:
    if word in join:
        join[word] +=1
    else:
        join[word] = 1
'''
print(join)
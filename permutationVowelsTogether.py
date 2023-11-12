import math
letter = input("Enter letters: ")
vowels = ''
vow = []
non = ''

for i in range(0,len(letter)):
    if (letter[i] in ['a','e','i','o','u']):
        vowels = vowels + letter[i]        
    else:
        non = non + letter[i]
vow.append(vowels)
total_fact = len(vow) + len(non)
vowels_fact = len(vowels)
permutation = (math.factorial(total_fact) * math.factorial(vowels_fact))
print("permutation vowels together :")
print(total_fact,"! ",' x ',vowels_fact,"! ",'= ',permutation)

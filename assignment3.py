#3.1
word = input("Enter a word: ")
vowel_count = 0
consonant_count = 0
vowels = []
consonants = []
for letter in word:
    if letter.lower() in "aeiou":
        vowel_count += 1
        vowels.append(letter)
    else:
        consonant_count += 1
        consonants.append(letter)
consonants.sort()
print("Vowels:", vowels)
print("Consonants:", consonants)

if vowel_count > consonant_count:
    print("Vowels have more characters.")
elif consonant_count > vowel_count:
    print("Consonants have more characters.")
else:
    print("The number of vowels and consonants is equal.")

#3.2
def length_of_last_word(s: str) ->int:
    s = s.strip()
    words = s.split()
    return len(words[-1]) if words else 0
s = str(input ("Enter the word:"))
print(length_of_last_word(s))

#3.3
num = int(input("enter any num: "))
numr = 0
while num != 0:
    d = num%10
    numr = numr*10 + d
    num//= 10
print(numr)

#3.4
def delchar(s, c):
    if len(c) != 1:
        return s
    return s.replace(c, '')
s = "Hello world "
c = "l"
result = delchar(s, c)
print(" The string after the character is removed:",result)

#3.5
def concatenate_alternate(s1, s2):
    result = ''
    for c1, c2 in zip(s1, s2):
        result += c1 + c2
    return result
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    return count
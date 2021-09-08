vowels = ['a', 'e', 'i', 'o', 'u', 'y']
created_string = input("Type in any string that you wish: ")
vowel_count = 0
for character in created_string:
    for letter in vowels:
        if character == letter:
            vowel_count +=1

print(vowel_count)

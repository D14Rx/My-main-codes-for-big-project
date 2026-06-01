#task 2:

vowel = ('a', 'e', 'i', 'o', 'u')

count = 0

word = input()

for char in word:
    if char in vowel:
        count += 1
        print(count)
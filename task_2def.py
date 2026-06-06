vowel = ('a', 'e', 'i', 'o', 'u')

word = input()

def tracking(vowel):

    count = 0

    for char in word:
        if char in vowel:
            count += 1
    return count

print(tracking(vowel))

if word == 'hello':
    print('world')
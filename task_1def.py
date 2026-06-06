text = input()

def reverse(text):

    reversed_words = []

    slices = text.split()
    for word in slices:
        w = word[::-1]
        reversed_words.append(w)        
    result = "".join(reversed_words)
    return result

print(reverse(text))
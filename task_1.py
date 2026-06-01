text = 'Try to reverse me!!!'

slices = text.split()

result = "".join(slices)

for word in slices:
    print(word[::-1])
n = int(input('Enter your number: '))

digits = [int(d) for d in str(n)]

result = sum(digits)

while result > 9:

    result = sum([int(d) for d in str(result)])

print(result)

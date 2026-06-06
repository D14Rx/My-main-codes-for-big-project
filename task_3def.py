n = int(input('Enter your number: '))

def till_1(n):

    digits = [int(d) for d in str(n)]

    result = sum(digits)

    while result > 9:
        result = sum([int(d) for d in str(result)])
    return result

print(till_1(n))
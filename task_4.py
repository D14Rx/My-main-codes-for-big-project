n = int(input('enter your number: '))
total = 0

splited = [int(d) for d in str(n)] #splited

lenght = len(str(n)) #lenght counted

for d in str(n):
        results = int(d) ** lenght        
        total += results

if total == n:
        print(True)
else:
    print(False)
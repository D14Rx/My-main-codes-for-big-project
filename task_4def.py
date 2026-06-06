n = int(input('enter your number: '))

def len_c(n):

        total = 0

        splited = [int(d) for d in str(n)] #splited

        lenght = len(str(n)) #lenght counted

        for d in str(n):
                results = int(d) ** lenght        
                total += results

        if total == n:
                return True
        else:
            return False

print(len_c(n))
n = int(input())
result = 0
for n in range(n+1):
    if n % 2 == 0:
        result = 2 ** n
        print(result)



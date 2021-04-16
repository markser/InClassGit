def possibleDivisor(n):
    x = 1
    while x <= n:
        if (n % x==0):
            print(x)
        x+=1
         
possibleDivisor(100)
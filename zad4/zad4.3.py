def factorial(n) :
    result=1
    for i in range(1, n+1):
        result*=i
    return result

silnia = int(input("Silnie jakiej liczby policzyc?\n"))

print(factorial(silnia))


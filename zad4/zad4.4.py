def fibonacci(n):
    a = 1
    b = 0
    for i  in range(n):
        temp=a
        a=b
        b= temp + b
    return b

fib = int(input("Ktory wyraz ciagu fibbonaciego policzyc?\n"))

print(fibonacci(fib))

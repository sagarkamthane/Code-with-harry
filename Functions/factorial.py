def factorial(n):
    fact = 1
    for i in range(n):
        fact = fact * (i+1)

    return fact

print(factorial(5))


def fact_recursive(n):
    if n==0 or n==1:
        return 1
    return n * fact_recursive(n-1)

print(fact_recursive(5))
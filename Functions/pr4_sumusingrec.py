def sumrec(n):
    if n<=0:
        return 0
    return n + sumrec(n-1)

print(sumrec(100))
def recursion(n):
    if n == 0:
        return 1
    print(n)
    return n * recursion(n - 1)

recursion(20)


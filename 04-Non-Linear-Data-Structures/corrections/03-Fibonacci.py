def fib(N):
    if N <= 1:
        return N
    return fib(N - 1) + fib(N - 2)

# print(fib(34))

def fib2(N):
    if N <= 1:
        return N;

    current = 0;
    prev1 = 1;
    prev2 = 0;

    for i in range(2, N + 1):
        current = prev1 + prev2;
        prev2 = prev1;
        prev1 = current;
    
    return current

print(fib2(34))
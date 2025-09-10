def fibonacci(n):
    """ Return the nth Fibonacci number. """
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
F = [0] * 1000 # Preallocate list for fibonacci numbers
F[0] = F[1] = 1 # Base cases

def rec_fib(n):
    """ Return the nth Fibonacci number using dynamic programming. """
    if F[n] != 0:
        return F[n]
    F[n] = rec_fib(n-1) + rec_fib(n-2)
    return F[n]

def iter_fib(n):
    """ Return the nth Fibonacci number using iterative approach. """
    F_iter = [0] * (n+1)
    F_iter[0] = F_iter[1] = 1
    for i in range(2, n + 1):
        F_iter[i] = F_iter[i-1] + F_iter[i-2]
    return F_iter[n]

def iter_fib_optimized(n):
    """ Return the nth Fibonacci number using optimized iterative approach. """
    if n <= 1:
        return 1
    F_prev, F_cur = 1, 1
    for _ in range(2, n + 1):
        F_prev, F_cur = F_cur, F_prev + F_cur
    return F_cur

def main():
    n = int(input("Enter a positive integer: "))
    print(f"The {n}th Fibonacci number is: {iter_fib_optimized(n)}")

if __name__ == "__main__":
    main()
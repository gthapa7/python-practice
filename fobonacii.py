# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end = " ")
#         a, b = b, a + b
# # fibonacci(19)
# def fib_recurssive(n):
#     if n <= 1:
#         return n
#     return fib_recurssive(n-1) + fib_recurssive(n-2)
# print(fib_recurssive(10))

# def sum(n):
#     if n <= 1:
#         return n
#     return sum(n-1) + sum(n-2)
# print(sum(20))

# def fib(n):
#     if n <= 1:
#         return n 
#     return fib(n-1) + fib(n-2)
# # print(fib(30))
# def fib_iterative(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a
# print(fib_iterative(10))


def print_fib_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
print(print_fib_sequence(11))
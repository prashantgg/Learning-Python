# n! = 1* 2 * 3* 4 * .... n 
# n! = [1* 2 * 3* 4 * .... n -1] *n
# n! = (n-1)! *n


# n = 4
# product = 1
# for i in range (n):
#     product = product * (i+1)
# print (product)

# def factorial_iter(n):
  
#     product = 1
#     for i in range (n):
#         product = product * (i+1)
#     return product
# f = factorial_iter(4)
# print(f)


# def factorial_recursive(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#      return n*factorial_recursive(n-1)


# f = factorial_recursive(4)
# print(f)


def fibonacci_series(n):
    if (n == 1):
        return 1
    elif (n == 0):
        return 0
    else:
        return fibonacci_series(n-1) + fibonacci_series (n-2)
    
for i in range(1):
    print (fibonacci_series(i))



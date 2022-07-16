# # 1 treating function as object
# def shout(text):
#     return text.upper()
#
#
# print(shout('Hello'))
# yell = shout
# print(yell('Hello'))
#
#
# # 2 Passing the function as an argument
# def shout(text):
#     return text.upper()
#
#
# def whisper(text):
#     return text.lower()
#
#
# def greet(func):
#     # storing the function in a variable
#     greeting = func("""Hi, I am created by a function passed as an argument.""")
#     print(greeting)
#
#
# greet(shout)
# greet(whisper)
#
#
# # 3 Returning functions from another function
# # 3.1
# def outer_adder(x):
#     def inner_adder(y):
#         return x+y
#
#     return inner_adder
#
#
# add_15 = outer_adder(15)
# print(add_15(10))
#
# # 4 Decorators
# def hello_decorator(function):
#     def inner1():
#         print("Hello, this is before function execution"
#         function()
#         print("This is after function execution")
#     return inner1
#
# def function_to_be_used():
#     print("This is inside the function !!")
#
#
# function_to_be_used = hello_decorator(function_to_be_used)
# # decorator duoc truyen vao function
# # function dc bo sung them decorator
# function_to_be_used()
#
# @hello_decorator
# def function_to_be_used():
#     print("This is inside the function !!")

# # 3.2
# import time
# import math
#
#
# def calculate_time(func):
#     def inner1(*args, **kwargs):
#         begin = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print("Total time taken in : ", func.__name__, end - begin)
#     return inner1
#
#
# @calculate_time
# def factorial(num):
#     time.sleep(2)
#     print(math.factorial(num))
#
#
# factorial(10)


# # 3.3
# def hello_decorator(func):
#     def inner1(*args, **kwargs):
#         print("before Execution")
#         returned_value = func(*args, **kwargs)
#         print("after Execution")
#         return returned_value
#     return inner1
#
#
# @hello_decorator
# def sum_two_numbers(a, b):
#     print("Inside the function")
#     return a + b
#
#
# a, b = 1, 2
# print("Sum =", sum_two_numbers(a, b))
#
# # WITHOUT DECORATOR
# # Inside the function
# # Sum = 3
#
# # WITH DECORATOR
# # before Execution
# # Inside the function
# # after Execution
# # Sum = 3

# # 3.4
# def decor1(func):
#     def inner():
#         x = func()
#         return x * x
#     return inner
#
#
# def decor(func):
#     def inner():
#         x = func()
#         return 2 * x
#     return inner
#
#
# @decor1
# @decor
# def num():
#     return 10
#
#
# print(num())
#
# decor1(decor(num))

# 3.5
import pydoc


def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging


@logged
def f(x):
   """does some math"""
   return x + x * x

print(f(5))
print(f.__name__)

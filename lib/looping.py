#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")

#Another way to do it with a while loop 
# def happy_new_year():
#     i+=10
#     while i > 0:
#         print(i)
#         i-= 1
#     if i == 0:
#         print("Happy New Year!")

def square_integers(int_list):
    int_list = [int ** 2 for int in int_list]
    return int_list
    # return [i ** 2 for i in int_list] shorthand notation

def fizzbuzz():
    for num in range(1, 101):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

#Another way to do it with while loop:

# def fizzbuzz():
#     i = 1
    
#     while i <= 100:
#         if not i % 15:
#             print("FizzBuzz")
#         elif not i % 5:
#             print("Buzz")
#         elif not i % 3:
#             print("Fizz")
#         else:
#             print(i)
#         i += 1

#test uses if not num % 15:  is dumb.. ¬_¬
# also, make sure that 15 is checked first as it is a multiple of 3 and 5 

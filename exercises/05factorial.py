# Write a method to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example method call
#
def factorial(num):
    newnum = num
    while num > 1:
        newnum = newnum*(num-1)
        num = num-1
    print(newnum);
factorial(5)
#
# > 120
#

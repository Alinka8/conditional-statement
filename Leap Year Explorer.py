# task 3 part 1: Leap your year

user=int(input("Input a year? "))

if (user % 4 == 0 and user%100 != 0) or (user%400 == 0):
    print (True)
    print("It is the leap year")
else:
    print (False)
    print("It is not the leap year")


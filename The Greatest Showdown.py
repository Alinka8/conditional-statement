# task 1 part 1: identify the greatest

# Write a Python program that prompts the user to enter three numbers. 
# The program should then identify and print out the largest number among the three.

first_number = int(input("Please enter the first number? "))
second_number=int(input("Please enter the second number? "))
third_number = int(input("Please enter the third number? "))


if first_number>second_number and first_number>third_number:
    print("The largest number: ", first_number)
elif second_number>first_number and second_number>third_number:
    print("The largest number ", second_number)
elif third_number>first_number and third_number>second_number:
    print("The largest number ", third_number)

# task 2 part 2: Identify the smallest
    # Extend your program from Task 1 to also determine the smallest number among the three and print it out.

first_number = int(input("Please enter the first number? "))
second_number=int(input("Please enter the second number? "))
third_number = int(input("Please enter the third number? "))


if first_number<second_number and first_number<third_number:
    print("The smallest number: ", first_number)
elif second_number<first_number and second_number<third_number:
    print("The smallest  number ", second_number)
elif third_number<first_number and third_number<second_number:
    print("The smallest number ", third_number)

# task 3 part 3: Equality check

def find_number(a,b,c):
    smallest=min(a,b,c)
    largest=max(a,b,c)

    if  a==b==c:
        print("All numbers are equal")
    elif a==b or a==b or b==c:
         equal_numbers = [num for num in (a,b,c) if num != smallest and num != largest ]
         print(f"The smallest number is {smallest}. The largest number is {largest}. There are two numbers equal to each other: {', '.join(map(str, equal_numbers))}")
    else:
        print(f"The smallest number is {smallest}. The largest number is {largest}")

# Test the function
find_number(3, 3, 4)


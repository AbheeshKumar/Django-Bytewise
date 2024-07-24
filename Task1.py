import random
import calendar


def Question_1():
    # Write a Python program that prints the string "Hello Python" to the console.
    print("Hello Python")


def Question_2():
    # Write a Python program that performs addition, subtraction, multiplication, and division of two numbers input by the user.
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def div(x, y):
        return x / y

    inp = int(
        input(
            "Press 1 for addition\nPress 2 for subtraction\nPress 3 for multiplication\nPress 4 for division\nEnter value: "
        )
    )

    x = int(input("Enter first value: "))
    y = int(input("Enter second value: "))
    ans = 0
    match inp:
        case 1:
            ans = add(x, y)
        case 2:
            ans = sub(x, y)
        case 3:
            ans = mul(x, y)
        case 4:
            ans = div(x, y)
        case _:
            print("Invalid Value")

    print("Final Answer", ans)


# Write a Python program to generate and print a random number between a specified range.
def Question_3():
    print(random.randint(10, 100))


# Write a Python program to display the calendar of a given month and year.
def Question_4():
    print(calendar.month(2001, 8))


# Write a Python program to check if a given year is a leap year.
def Question_5():
    inp = int(input("Enter a year: "))

    if inp % 4 == 0:
        if inp % 100 == 0:
            if inp % 400 == 0:
                print(inp, "is a leap year")
            else:
                print(inp, "is not a leap year")
        else:
            print(inp, "is a leap year")
    else:
        print(inp, "is not a leap year")


# Write a Python program to print all prime numbers within a specified range.
def Question_6():
    num = 15
    prime_ls = []
    for i in range(num):
        count = 0
        for j in range(num):
            if (i + 1) % (j + 1) == 0:
                count += 1
        if count == 2:
            prime_ls.append(i + 1)
    print(prime_ls)


# Write a Python program to find the factorial of a number input by the user.
def Question_7():
    num = int(input("Enter a factorial number: "))
    fact_num = 0
    for i in range(num):
        if i == 0:
            fact_num = num
        elif i == num:
            continue
        else:
            fact_num = fact_num * (num - (i))
    print(fact_num)


# Write a Python program to print the Fibonacci sequence up to a specified number of terms.
# 0 1 1 2 3 5 8 13
def Question_8():
    fib_series = [0, 1]
    num = 6
    fib = 0
    old_num, new_num = 0, 1
    for i in range(num):
        fib = old_num + new_num
        fib_series.append(fib)
        old_num, new_num = new_num, fib
    print(fib_series)


# Write a Python program to find all Armstrong numbers within a specified range.
def Question_9():
    rnge = 2000
    for i in range(rnge):
        num = str(i)
        length = len(num)
        arms_num = 0
        for j in num:
            arms_num = arms_num + int(j) ** length
        if arms_num == i:
            print(i)


# Write a Python program to print the reverse of a string input by the user.
def Question_10():
    inp = input("Enter a string: ")
    print(inp[::-1])


# Write a Python program to calculate and print the sum of the first ten natural numbers.
def Question_11():
    nat_sum = 0
    for i in range(10):
        nat_sum += i + 1
    print(nat_sum)


# Call whichever function/Question you want

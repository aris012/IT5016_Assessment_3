#Practice handling basic errors using try-expect block

try:
    first_number = int(input("Please input the first number: "))
    second_number = int(input("Please input the second number: "))
    result = first_number/second_number
    print(int(result))
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero!")
except ValueError as e:
    print(e)
    print("Enter only numbers")
except Exception as e:
    print(e)
    print("Something went wrong...")
else:
    print(result)
finally:
    print("This will always execute")
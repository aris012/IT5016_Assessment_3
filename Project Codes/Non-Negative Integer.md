## Non-negative Integer as its parameter
#### Python function that takes a non-negative integer as its parameter. The function should calculate the factorial of that number and return the result.

        def factorial (num):
            if num == 0:
                return 1
            else:
                return num * factorial (num-1)  
        num = int(input("Enter the number : "))
        print("The factorial is : ", factorial(num))

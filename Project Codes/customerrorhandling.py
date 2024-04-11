#Custom Error Handling

class NegativeNumberError(Exception):
    def _init_(self,value):
        self.value = value

try:
    number = int(input("Please enter a number..."))
    if number < 0 :
        raise NegativeNumberError("Sorry you entered a negative integer")
    print(f"You entered {number}")

except ValueError as e:
    print(e)

except NegativeNumberError as e:
    print(e)
 
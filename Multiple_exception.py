class NegativeNumberError(Exception):
    pass
def calculate(number):
    if num < 0:
        raise NegativeNumberError("Cannot calculate square root of a negative number.")
    return number ** 0.5
try:
    num = int(input("Enter number: "))
    if not num.strip():
        raise ValueError("Input cannot be empty.")
    num = float(num)
    result = calculate(num)
    print(f"Result: {result}")
except ValueError as e:
    print("An error occured: {e}")
except NegativeNumberError as e:
    print("An error occured: {e}")
except Exception as e:
    print("An unexpected error occured")
finally:
    print("Program execution finished")
import math

number = float(input("Enter a number: "))


square_root = math.sqrt(number)


if number > 0:
    natural_log = math.log(number)
else:
    natural_log = "undefined (logarithm of non-positive number is not defined)"

sine_value = math.sin(number)

print(f"\nResults for the number {number}:")
print(f"Square root: {square_root}")
print(f"Natural logarithm (log base e): {natural_log}")
print(f"Sine (in radians): {sine_value}")

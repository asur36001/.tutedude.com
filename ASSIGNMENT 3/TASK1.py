# Step 1: Define the factorial function using a loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Step 3: Call the function with a sample number and print the output
sample_number = 5
print(f"The factorial of {sample_number} is:", factorial(sample_number))

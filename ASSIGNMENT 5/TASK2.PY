def main():
    # Step 1: Create a list of numbers from 1 to 10
    numbers = list(range(1, 11))

    # Step 2: Extract the first five elements from the list
    extracted_elements = numbers[:5]

    # Step 3: Reverse the extracted elements
    reversed_elements = extracted_elements[::-1]

    # Step 4: Print both the extracted list and the reversed list
    print("Extracted elements:", extracted_elements)
    print("Reversed elements:", reversed_elements)

# Run the main function
if __name__ == "__main__":
    main()

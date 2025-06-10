def main():
    # Step 1: Create a dictionary of student names and their marks
    student_marks = {
        'Alice': 85,
        'Bob': 78,
        'Charlie': 92,
        'David': 88,
        'Eva': 95
    }

    # Step 2: Ask the user to input a student's name
    student_name = input("Enter the student's name: ")

    # Step 3: Retrieve and display the corresponding marks
    if student_name in student_marks:
        print(f"{student_name}'s marks: {student_marks[student_name]}")
    else:
        # Step 4: Display an appropriate message if the name is not found
        print(f"Error: Student '{student_name}' not found in the records.")

# Run the main function
if __name__ == "__main__":
    main()

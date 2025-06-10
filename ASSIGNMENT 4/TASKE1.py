def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line.strip())  # Print each line without extra newline characters
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")

# Specify the file name
file_name = 'Sample.txt'
read_file(file_name)

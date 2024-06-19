input_string = input("Enter a string: ")
with open("my_file.txt", "w") as f:
    # Write the input string to the file.
    f.write(input_string)
f.close()
print("The string has been written to the file.")
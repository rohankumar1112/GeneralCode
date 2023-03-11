# Open the input file for reading
with open('data.txt', 'r') as f:
    # Read the contents of the file into a string
    data = f.read()

# Convert the string to lowercase
lowercase_data = data.lower()

# Open the output file for writing
with open('data2.txt', 'w') as f:
    # Write the lowercase string to the output file
    f.write(lowercase_data)

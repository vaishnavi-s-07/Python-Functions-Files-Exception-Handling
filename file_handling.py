# Python File Handling

# Writing into a file
with open("student.txt", "w") as file:
    file.write("Welcome to Python File Handling!\n")
    file.write("Student Name: Vaishnavi\n")

# Reading the file
with open("student.txt", "r") as file:
    content = file.read()
    print(content)

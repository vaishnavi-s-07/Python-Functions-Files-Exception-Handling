import json

student = {
    "name": "Vaishnavi",
    "department": "CSE",
    "marks": 90
}

# Write JSON file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

# Read JSON file
with open("student.json", "r") as file:
    data = json.load(file)

print("Student Details:")
print("Name:", data["name"])
print("Department:", data["department"])
print("Marks:", data["marks"])

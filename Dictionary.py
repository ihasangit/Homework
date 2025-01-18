# Create a dictionary for the dog
dog = {
    "name": "Baga",
    "color": "Offwhite",
    "breed": "Bangladeshi",
    "legs": 4,
    "age": 3
}

# Create a dictionary for the student
student = {
    "first_name": "Maruf",
    "last_name": "Antor",
    "gender": "Male",
    "age": 26,
    "marital_status": "married",
    "skills": ["Python", "Java", "SQL","C++"],
    "country": "USA",
    "city": "New York",
    "address": "1234 Church mcdonald"
}

# Get the length of the student dictionary
student_length = len(student)

# Get the value of skills and check its data type
skills = student["skills"]
skills_type = type(skills)

# Print the results
print("Dog Dictionary:", dog)
print("Student Dictionary:", student)
print("Length of Student Dictionary:", student_length)
print("Skills:", skills)
print("Data Type of Skills:", skills_type)


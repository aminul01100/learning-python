"""
# primary approach before learning about lists
course_1_gpa = 3.5
course_2_gpa = 3.8
course_3_gpa = 3.2
course_4_gpa = 3.9
course_5_gpa = 3.6

# we can use a list to store the GPAs of the courses instead of 
# declaring separate variables for each course
course_gpas = [3.5, 3.8, 3.2, 3.9, 3.6]
# meaning of the list - course_gpas:
# course_gpas[0] = 3.5
# course_gpas[1] = 3.8
# course_gpas[2] = 3.2
# course_gpas[3] = 3.9
# course_gpas[4] = 3.6

# calculating average GPA using the list
total_gpa = 0
position = 0
while position < 5:
    total_gpa = total_gpa + course_gpas[position]
    position = position + 1

average_gpa = total_gpa / 5 
print("Average GPA: ", average_gpa)
"""

"""
problem statement: 
we want to calculate the average GPA of a student who has taken N courses. 
We can use a list to store the GPAs of the courses and then calculate the average using a loop.

User will input the number of courses and then input the GPA for each course. 
We will store the GPAs in a list and then calculate the average GPA.
"""
""" 
# solution: 
number_of_courses = int(input("Enter the number of courses: "))
course_gpas = []

counter = 0
while counter < number_of_courses:
    gpa = input("Enter the GPA for course " + str(counter + 1) + ": ")
    gpa = float(gpa)  # convert string to float
    course_gpas.append(gpa)  # add the GPA to the list
    counter = counter + 1

print("Course GPAs: ", course_gpas)

position = 0
total_gpa = 0
while position < number_of_courses:
    total_gpa = total_gpa + course_gpas[position]
    position = position + 1

print("Total GPA: ", total_gpa)
average_gpa = total_gpa / number_of_courses
print("Average GPA: ", round(average_gpa, 2))  # round the average GPA to 2 decimal places
"""

"""
random_list = [1, 2, 3, 4, 5]
random_list.pop() # removes the last element from the list
random_list.remove(2) # removes the first occurrence of the value 2 from the list
print(random_list)
print("Length of the list: ", len(random_list)) # prints the length of the list

random_list.append(6) # adds the value 6 to the end of the list
print(random_list)
"""

# Discussing set
"""
# initializing a set
unique_numbers_set = {1, 2, 3, 4, 5}
print(unique_numbers_set)

# taking different type of data in a list
student_district_list = ["Dhaka", "Chittagong", "Khulna", "Rajshahi", "Barisal", 
                        "Barisal", "Chittagong", "Dhaka", "Sylhet", "Rangpur"]
unique_districts = set(student_district_list) # using set to get unique districts
# unique_districts_list = list(unique_districts) # converting the set back to a list
unique_districts_sorted = sorted(unique_districts) # sorting the list of unique districts
# print("Unique Districts: ", unique_districts_sorted)

# index = 0
# while index < len(student_district_list):
#     print("District: ", student_district_list[index])
#     index = index + 1

for index in range(5, 10, 2):
    print("District: ", student_district_list[index])

# range(start, stop, step) - generates a sequence of numbers from start to stop with a step (increment/decrement)
# range(5, 10, 2) - generates the numbers 5, 7, 9 (start=5, stop=10, step=2)
"""
# discussing dictionary

student_roll_name_dict = {
    1: "Abul",
    2: "Babul",
    3: "Cabul",
    4: "Dabul",
    5: "Ebul"
}
student_roll_name_dict[6] = "Fabul" # adding a new key-value pair to the dictionary
student_roll_name_dict.pop(2) # removes the key-value pair with key 2 from the dictionary

# print(student_roll_name_dict) # prints the name of the student with roll number 3, 3 is key and "Cabul" is value

# for key in student_roll_name_dict:
#     print("Roll Number: ", key, ", Name: ", student_roll_name_dict[key]) # prints the roll number and name of each student in the dictionary

# print(student_roll_name_dict.items()) # prints the key-value pairs of the dictionary as a list of tuples

# for key, value in student_roll_name_dict.items():
#     print("Roll Number: ", key, ", Name: ", value) # prints the roll number and name of each student in the dictionary

# print(student_roll_name_dict.keys()) # prints the keys of the dictionary
# print(student_roll_name_dict.values()) # prints the values of the dictionary

students_roll_marks_dict = {
    1: 100,
    2: 90,
    3: 78,
    4: 92,
    5: 87,
    6: 35
}
number_list = students_roll_marks_dict.values()
# total_marks = 0
# for mark in number_list:
#     total_marks = total_marks + mark

total_marks = sum(number_list) # using the built-in sum function to calculate the total marks

average_marks = total_marks / len(students_roll_marks_dict) if len(students_roll_marks_dict) > 0 else 0
print("Average Marks: ", round(average_marks, 2)) # round the average marks to 2 decimal places


student_info_list = []
while True:
    roll_number = input("Enter the roll number of the student to get the marks (or 'exit' to quit): ")
    if roll_number == "exit":
        break
    roll_number = int(roll_number) # convert the input to an integer

    student_age = input("Enter the age of the student: ")
    student_age = int(student_age) # convert the input to an integer

    student_name = input("Enter the name of the student: ")

    student_info = {
        "roll_number": roll_number,
        "age": student_age,
        "name": student_name
    }
    student_info_list.append(student_info) # add the student info dictionary to the list

# print("Student Information: ", student_info_list)
for student in student_info_list:
    print("Roll Number: ", student["roll_number"], ", Age: ", student["age"], ", Name: ", student["name"])
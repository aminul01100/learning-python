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

random_list = [1, 2, 3, 4, 5]
random_list.pop() # removes the last element from the list
random_list.remove(2) # removes the first occurrence of the value 2 from the list
print(random_list)
print("Length of the list: ", len(random_list)) # prints the length of the list


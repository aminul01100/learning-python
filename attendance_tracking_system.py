"""
problem statement:
attendance tracking system
('Bob', '10:15 AM'),
we have a set of students - number of students - 5

we need track their attendance of 5 days in a week. (mon-fri)

functionalities:
    1. the system can search for any student at any day to see if the student was present or not 
        (input - student name and day, output - present/absent)
    2. the system can say the days the specified student was a late comer 
        (input - student name, output - day and late time)
    3. the system can say the absent records for each day 
        (input - day, output - list of absent students)
"""

student_list = ["Alice", "Bob", "Charlie", "David", "Eve"]

attendance_records = {
    "Monday": [('Alice', '8:00 AM'), ('Bob', '10:15 AM'), ('Charlie', 'Absent'), ('David', '8:00 AM'), ('Eve', '8:00 AM')],
    "Tuesday": [('Alice', '8:00 AM'), ('David', '8:00 AM'), ('Eve', '8:00 AM')],
    "Wednesday": [('Bob', '10:15 AM'), ('Charlie', 'Absent'), ('David', '8:00 AM'), ('Eve', '8:00 AM')],
    "Thursday": [('Alice', '8:00 AM'), ('Charlie', 'Absent'), ('Eve', '8:00 AM')],
    "Friday": [('David', '8:00 AM'), ('Eve', '8:00 AM')]
}

# functionality 1
def check_attendance():
    """
    the system can search for any student at any day to see if the student was present or not 
    (input - student name and day, output - present/absent)
    """
    student_name = input("Enter student name: ")
    day = input("Enter day (Monday-Friday): ")

    attendance = attendance_records.get(day, "not found")
    if attendance == "not found":
        print("Invalid day entered.")
        return

    is_present = False
    for name, time in attendance:
        if name.lower() == student_name.lower():
            is_present = True
            print(f"{student_name} was present on {day}.")
            break
    if not is_present:
        print(f"{student_name} was absent on {day}.")


# functionality 2
def find_late_coming_days():
    """
    the system can say the days the specified student was a late comer 
    (input - student name, output - day and late time)
    """
    student_name = input("Enter student name: ")
    for day, attendance in attendance_records.items():
        for name, time in attendance:
            if name.lower() == student_name.lower() and time != '8:00 AM':
                print(f"{student_name} was a late comer on {day} at {time}.")
                break

print("Functionality 1: Check Attendance")
print("Functionality 2: Find Late Coming Days")

input_choice = input("Enter functionality number (1 or 2): ")
if input_choice == '1':
    print("Attendance Checking System:")
    check_attendance()
elif input_choice == '2':
    print("Late Coming Days System:")
    find_late_coming_days()

# barir kaj
"""
1. the system will support uppercase and lowercase input for student names and days
2. complete functionality number three
3. add input validation for these functionalities
"""
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
import logging

logger = logging.getLogger(__name__)

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

    try:
        attendance = attendance_records.get(day, None)
        if attendance == None:
            logger.info("Invalid day entered.")
            return

        is_present = False
        for name, time in attendance:
            if name.lower() == student_name.lower():
                is_present = True
                logger.info(f"{student_name} was present on {day}.")
                break
        if not is_present:
            logger.info(f"{student_name} was absent on {day}.")

    except Exception as error:
        logger.error(f"An error occurred: {error}", exc_info=True)


# functionality 2
def find_late_coming_days():
    """
    the system can say the days the specified student was a late comer 
    (input - student name, output - day and late time)
    """
    student_name = input("Enter student name: ")
    try:
        for day, attendance in attendance_records.items():
            for name, time in attendance:
                if name.lower() == student_name.lower() and time != '8:00 AM':
                    logger.info(f"{student_name} was a late comer on {day} at {time}.")
                    break
    except Exception as error:
        logger.error(f"An error occurred: {error}", exc_info=True)


while True:
    logger.info("Choose a functionality and write 'quit' to exit:")
    logger.info("Functionality 1: Check Attendance")
    logger.info("Functionality 2: Find Late Coming Days")

    input_choice = input("Enter functionality number (1 or 2): ")
    if input_choice.lower() == 'quit':
        logger.info("Exiting the system. Goodbye!")
        break

    if input_choice == '1':
        logger.info("Attendance Checking System:")
        check_attendance()
    elif input_choice == '2':
        logger.info("Late Coming Days System:")
        find_late_coming_days()

# barir kaj
"""
1. the system will support uppercase and lowercase input for student names and days
2. complete functionality number three
3. add input validation for these functionalities
"""
# !/usr/bin/env python3
# Emily Ho
# 335693420
# OOP Assessment
# Student registration and course selection of a high school

from person import Person, Student, Teacher
from registration import Registration

register = True
# The while loop is so that if the you want to register another student, the program will restart instead of exiting.
while register:
    # Ask for the school name
    schoolName = input("Enter school name: ")
    school1 = Registration(schoolName)
    school1.welcome()

    # Ask for student's first and last name
    fName = input("Enter First Name: ")
    lName = input("Enter Last Name: ")

    # Inner while loop is used to re-prompt the student if the grade that they typed is not a number from 9 to 12
    while True:
        grade = input("Enter grade (9-12): ")
        if grade.isdigit() and int(grade) >= 9 and int(grade) <= 12:
            break
        else:
            continue
    # End of inner while loop

    # Inner while loop is used to re-prompt the student if the ID is not a number
    while True:
        id = input("Enter your student ID: ")
        if id.isdigit():
            break
        else:
            continue
    # End of inner while loop

    # Create Student object from a Person object (Student will be the user)
    student1 = Person(fName, lName)
    student1 = Student(student1.getFName(), student1.getLName(), grade, id)

    # Create teacher objects from a Person object
    # The teachers will all have a different subject to teach, but they will teach all high school grades
    teacher1 = Person("Mr.", "Park")
    teacher1 = Teacher(teacher1.getFName(), teacher1.getLName(), "Computers")
    teacher2 = Person("Mrs.", "Smith")
    teacher2 = Teacher(teacher2.getFName(), teacher2.getLName(), "Math")
    teacher3 = Person("Mrs.", "Tissue")
    teacher3 = Teacher(teacher3.getFName(), teacher3.getLName(), "Science")
    teacher4 = Person("Mrs.", "Johnson")
    teacher4 = Teacher(teacher4.getFName(), teacher4.getLName(), "French")
    teacher5 = Person("Mr.", "Hansel")
    teacher5 = Teacher(teacher5.getFName(), teacher5.getLName(), "English")
    teacher6 = Person("Mrs.", "Bell")
    teacher6 = Teacher(teacher6.getFName(), teacher6.getLName(), "Geography")
    teacher7 = Person("Mr.", "Berkley")
    teacher7 = Teacher(teacher7.getFName(), teacher7.getLName(), "History")
    teacher8 = Person("Mrs.", "Dawn")
    teacher8 = Teacher(teacher8.getFName(), teacher8.getLName(), "Art")
    teacher9 = Person("Mr.", "Wonka")
    teacher9 = Teacher(teacher9.getFName(), teacher9.getLName(), "Music")
    teacher10 = Person("Mr.", "Wood")
    teacher10 = Teacher(teacher10.getFName(), teacher10.getLName(), "Business")
    teacher11 = Person("Mrs.", "Kendall")
    teacher11 = Teacher(teacher11.getFName(), teacher11.getLName(), "Law")
    teacher12 = Person("Mr.", "Davidson")
    teacher12 = Teacher(teacher12.getFName(), teacher12.getLName(), "Drama")
    teacher13 = Person("Mrs.", "Greene")
    teacher13 = Teacher(teacher13.getFName(), teacher13.getLName(), "Accounting")
    teacher14 = Person("Mr.", "Balloon")
    teacher14 = Teacher(teacher14.getFName(), teacher14.getLName(), "Gym")
    print("-" * 50)

    # After student enters all their information, he/she is able to speak to someone.
    # This allows the student to greet that person and start selecting courses.
    student1.greet()
    print("-" * 50)

    # The registration system greets/welcomes the student
    Registration.greet(student1.getFName())

    # Print a specific message to the student based on their grade
    print(student1.gradeCheck())
    print("-"*50)

    # Set student's timetable based on courses they selected
    semester = Registration.setCourses(student1.getFName(), student1.getFName())
    print("-" * 50)

    # Output the teacher that the student will have based on their timetable (Only for the first semester)
    print("First Semester:")
    Teacher.hTeach(teacher1, semester)
    Teacher.hTeach(teacher2, semester)
    Teacher.hTeach(teacher3, semester)
    Teacher.hTeach(teacher4, semester)
    Teacher.hTeach(teacher5, semester)
    Teacher.hTeach(teacher6, semester)
    Teacher.hTeach(teacher7, semester)
    Teacher.hTeach(teacher8, semester)
    Teacher.hTeach(teacher9, semester)
    Teacher.hTeach(teacher10, semester)
    Teacher.hTeach(teacher11, semester)
    Teacher.hTeach(teacher12, semester)
    Teacher.hTeach(teacher13, semester)
    Teacher.hTeach(teacher14, semester)
    print("-" * 50)

    # Once student received his/her timetable, they have a choice to exit the system or let another student register.
    Registration.signOut(school1)


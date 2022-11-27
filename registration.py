# Registration Class

from random import randrange

class Registration:
    ''' This class represents a school registration system where students are able to select courses and get their timetables '''

    # Initialization method
    def __init__(self, school):
        self.__school = school

    # __str__() base function converts the object to a string
    def __str__(self):
        return self.__school

    # Method that welcomes the student to the school
    def welcome(self):
        print("Welcome to %s !" % self.__school)
    # End of welcome method

    # This method is an example of polymorphism because it is also used in the Person class
    # It greets the student into the Registration System
    def greet(self):
        print("Hello %s! Welcome to the School Registration System." % (self))
    # End of greet method

    # Method that returns a list of high school courses for the student to choose from
    def hCourses(self):
        hCourseList = ["Math", "Science", "French", "English", "Computers", "Geography", "History", "Art", "Music",
                        "Business", "Law", "Drama", "Accounting", "Gym"]
        return hCourseList
    # End of hCourses method

    # Method that allows the student to select their courses for the year
    def selectCourse(self):
        # Empty list for student's chosen courses
        selected = []
        coursePrompt = True
        while coursePrompt:
            print("Enter the 8 courses you want to take this year.")
            print((" --> Note: If course name is incorrectly spelled, it might interfere with your course selection."))

            # This prints the list of courses from the hCourses method
            print("Here is a list of courses:\n", Registration.hCourses(self))
            print("")
            counter = 1
            # Check if selected list has 8 courses
            while len(selected) != 8:
                courseList = Registration.hCourses(self)
                # Ask student to enter their course choices based on the course list
                # counter is used to count the number of courses the student has chosen so far
                course = input("Enter course #%d: " % int(counter))
                # Capitalize the user input so that it matches the subjects in the course list and the subjects the teachers are teaching
                course = course.capitalize()
                # Go through each letter in course(user input)
                for letters in range(len(course)):
                    # Go through each item in the courseList
                    for values in range(len(courseList)):
                        # Check if the course that the student typed matches a subject in courseList
                        if course == courseList[values]:
                            # Check if the course is not in selected list
                            if course not in selected:
                                # If all conditions above are met, add course to the selected list
                                selected.append(course)
                                # counter only counts when user input matches the above conditions
                                counter+=1
                                break
                            # If no condition above is met, re-prompt user to enter another course
                            else:
                                continue
                    # End of inner for loop
                # End of for loop
            # End of inner while loop

            # Output the list of courses that the student selected
            print("These are your choices:\n", selected)
            rePrompt = True
            while rePrompt:
                # Ask if the student is satisfied with the courses they selected
                courseCheck = input("Are you sure you want to take these courses? (yes or no): ")
                # If student types 'yes', exit both while loops.
                if courseCheck.lower() == "yes":
                    print("Ok, we are processing your requests.\n...")
                    rePrompt = False
                    coursePrompt = False

                # If student types 'no', exit the inner while loop, and re-prompt student to enter their course choices
                elif courseCheck.lower() == "no":
                    selected.clear()
                    rePrompt = False
                    coursePrompt = True

                # If student does not type 'yes' or 'no', ask student to re-type their answer to this question
                else:
                    rePrompt = True
                    coursePrompt = False
            # End of inner while loop
        # End of while loop
        # Return the student's selected course list so that it can be accessible through other methods
        return selected
    # End of selectCourse method

    # Method that sets the student's timetable based on the courses they chose
    def setCourses(self, name):
        semester1 = []
        semester2 = []
        # Get the student's list of chosen courses from the selectCourse method
        courses = Registration.selectCourse(name)

        for items in range(4):
            # Check if semester1 list does not have 4 courses
            while len(semester1) != 4:
                # Randomly choose courses for student's 1st semester(based on their chosen courses)
                randCourse = randrange(len(courses))
                # Check if the random course is not already in semester1 list
                if courses[randCourse] not in semester1:
                    # The courses are added to the semester1 list
                    semester1.append(courses[randCourse])

            # This executes if semester1 list has 4 courses
            else:
                # Check if semester2 list does not have 4 courses
                while len(semester2) != 4:
                    # Randomly choose courses for student's 2nd semester(based on their chosen courses)
                    randCourse2 = randrange(len(courses))
                    # Check if the random course is not already in semester1 or semester2 list
                    if courses[randCourse2] not in semester1:
                        if courses[randCourse2] not in semester2:
                            # The courses are added to the semester2 list
                            semester2.append(courses[randCourse2])
                # End of while loop
            # End of while...else loop

        # Output student's timetables for semester 1 and 2
        print(name, "'s semester 1:", semester1)
        print(name, "'s semester 2:", semester2)
        # Return semester1 list to access the student's teachers for 1st semester
        return semester1
    # End of setCourses method

    # Method that allows students to sign-out of the registration system
    def signOut(self):
        while True:
            # Ask user if they want to leave the Registration System
            finish = input("Would you like to exit the system or register another student? (Enter 'Exit' or 'Register'): ")
            # If student types 'exit', the program ends
            if finish.lower() == "exit":
                exit()
            # If student types 'register', the program loops from the beginning
            elif  finish.lower() == "register":
                break
            # If student types anything else that is not 'exit' or 'register', re-ask this question
            else:
                continue
        # End of while loop
    # End of signOut Method
# End of Registration Class
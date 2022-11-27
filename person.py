# Person, Student, Teacher Class

class Person:
    ''' This class represents any type of person belonging to a school. '''

    # Initialization method
    def __init__(self, fName, lName):
        self.__fName = fName
        self.__lName = lName

    # Since first name is encapsulated, this method allows us to access the first name outside of this class
    def getFName(self):
        return self.__fName

    # Since last name is encapsulated, this method allows us to access the last name outside of this class
    def getLName(self):
        return self.__lName

    #__repr__() base function returns a string that contains a printable version of the object
    def __repr__(self):
        return ("%s %s") % self.__fName, self.__lName

    # __str__() base function converts the object to a string
    # This allows the Person class to have a string representation of their first and last name
    def __str__(self):
        return ("%s %s") % self.__fName, self.__lName

    # This method is an example of polymorphism because it is also used in the Registration class
    # After student enters all their information, he/she is able to speak to someone.
    # This allows the student to greet and say what they want to do in the registration system.
    def greet(self):
        print("Hi, my name is %s %s. I want to register for school and get my timetable." % (self.__fName, self.__lName))
    # End of greet method
# End of Person Class

class Student(Person):
    ''' This class inherits from the parent class and it represents a student '''

    # Initialization method
    def __init__(self, fName, lName, grade, id):
        # super() takes the attributes from the Person class
        super().__init__(fName, lName)
        self.__grade = grade
        self.__id = id

    # This method outputs a little message based on student's grade
    def gradeCheck(self):
        if self.__grade == "12":
            return "Since you are in grade 12, you will be graduating this year. Congratulations %s!" % (self.getFName())

        elif self.__grade == "11":
            return "Since you are in grade 11, your marks may count towards your post-secondary applications. Keep working hard %s!" % (self.getFName())

        elif self.__grade == "10":
            return "%s, since you are in grade 10, you have to write the OSSLT test this year." % (self.getFName())

        elif self.__grade == "9":
            return "Welcome to high school! This year, you get to meet new people!"
    # End of gradeCheck method
# End of Student Class

class Teacher(Person):
    ''' This class inherits from the parent class and it represents a teacher '''

    # Initialization method
    def __init__(self, fName, lName, teachSubject):
        # super() takes the attributes from Person class
        super().__init__(fName, lName)
        self.__teachSubject = teachSubject

    # This method checks which teacher will teach the student based on their 1st semester courses
    def hTeach(self, subject):
        # Iterate through the list of subjects in the student's semester1 timetable
        for item in range(len(subject)):
            # Check if the teacher is teaching the student by subject
            if self.__teachSubject in subject[item]:
                # Output student's timetable with teachers
                print("Period %d: %s : %s %s" % (item+1, subject[item], self.getFName(), self.getLName()))
        # End of for loop
    # End of hTeach method
# End of Teacher Class



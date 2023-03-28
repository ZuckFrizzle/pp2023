

class Course:
    def __init__(self, course_id, name):
        self.__course_id = course_id
        self.__name = name

    def getCourseID(self):
        return self.__course_id

    def getName(self):
        return self.__name
    
class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob

    def getStudentID(self):
        return self.__student_id
    
    def getName(self):
        return self.__name

    def getDob(self):
        return self.__dob


class Mark:
    def __init__(self, mark):
        self.__mark = mark

    def getMark(self):
        return self.__mark

class Major:
    def __init__(self):
        self.__studentIndic = {}
        self.__courseIndic = {}
        self.__markIndic = {}

    def getStudentIndic(self):
        return self.__studentIndic
    
    def getCourseIndic(self):
        return self.__courseIndic

    def getMarkIndic(self):
        return self.__markIndic
    
    # Value ventilator
    def checkValue(self, num):
        try:
            num = int(num)
        except ValueError:
            print("Integers only please!\n")
            return
        if (num >= 0):
            return int(num)
        else:
            print("Accept only positive value!\n")

    # Input number of students in a class

    def studentNum(self):
        while True:
            studentNum = input("Enter the number of students in a class: ")
            if self.checkValue(studentNum):
                return int(studentNum)
        
    # Input number of courses

    def courseNum(self):
        while True:
            courseNum = input("Enter the number of courses: ")
            if self.checkValue(courseNum):
                return int(courseNum)

    # Input student information: id, name, DoB

    def studentInfo(self):
        numOfStudents = self.studentNum()
        for i in range(numOfStudents):
            id = input("Enter the student ID: ")
            name = input("Enter the student name: ")
            dob = input("Enter the student dob: ")
            self.__studentIndic[id] = Student(id, name, dob)

    # Input course information: id, name

    def courseInfo(self):
        numOfCourses = self.courseNum()
        for i in range(numOfCourses):
            id = input("Enter the course id: ")
            name = input("Enter the course name: ")
            self.__courseIndic[id] = Course(id, name)

    # Select a course, input marks for student in this course

    def mark(self):
        courseID = input("Enter the courseID: ")
        if courseID not in self.__courseIndic:
            print("Invalid course ID!")
            return
        for studentID in self.__studentIndic:
            mark = float(input(f"Enter the mark for {self.__studentIndic[studentID].getName()}: "))
            while mark < 0 or mark > 20:
             print(f"Invalid mark for id {self.__studentIndic[studentID].getName()}")
            if studentID not in self.__markIndic:
                self.__markIndic[studentID] = {}
            self.__markIndic[studentID][courseID] = mark

    # List courses

    def courseList(self, course_id):
        print(f"{course_id}: {self.__courseIndic[course_id].getName()}")
            
    # List students

    def studentList(self, student_id):
        print(f"+) {student_id}: {self.__studentIndic[student_id].getName()}")
        
    # Show student marks for a given course

    def displayMark(self):
        courseID = input("Enter the course ID: ")
        if courseID not in self.__courseIndic:
            print("Course ID is not valid, please type again!")
            return
        for studentID in self.__studentIndic:
            if studentID in self.__markIndic and courseID in self.__markIndic[studentID]:
                print(f"{self.__studentIndic[studentID].getName()}: {self.__markIndic[studentID][courseID]}")
            else:
                print(f"{self.__studentIndic[studentID].getName()}: Not exist")

    # Show everything including students and courses

    def allCourse(self):
        for courseID in self.__courseIndic:
            self.courseList(courseID)
            for studentID in self.__studentIndic:
                self.studentList(studentID)



major = Major()
major.studentInfo()
major.courseInfo()

while True:
    print("Take a choice: ")
    print("1. Input marks for a course")
    print("2. Display all course")
    print("3. Display mark list")
    print("4. Quit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        major.mark()
    elif choice == 2:
        major.allCourse()
    elif choice == 3:
        major.displayMark()
    elif choice == 4:
        break
    else:
        print("Choice proves to be error!")
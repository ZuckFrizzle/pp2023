studentIndic = {}
courseIndic = {}
markIndic = {}

# Input the quantity of students per class

def studentNum():
    return int(input("Enter the number of students in a class: "))

# Input the quantity of courses

def courseNum():
    return int(input("Enter the number of courses: "))

# Input the basic of student: id, name, DoB

def studentInfo():
    numOfStudents = studentNum()
    for i in range(numOfStudents):
        id = input("Enter the student ID: ")
        name = input("Enter the student name: ")
        dob = input("Enter the student dob: ")
        studentIndic[id] = {"name": name, "dob": dob}

# Input the basic of course: id, name

def courseInfo():
    numOfCourses = courseNum()
    for i in range(numOfCourses):
        id = input("Enter the course ID: ")
        name = input("Enter the course name: ")
        courseIndic[id] = {"name": name}

# Choose a course, input marks for students in this course

def mark():
    course_id = input("Enter the course ID: ")
    if course_id not in courseIndic:
        print("Course ID is not valid, please type again!")
        return
    for student_id in studentIndic:
        mark = float(input(f"Enter the mark for {studentIndic[student_id]['name']}: "))
        while mark < 0 or mark > 20:
             print(f"Invalid mark for id {studentIndic[student_id]['name']}")
        if student_id not in markIndic:
            markIndic[student_id] = {}
        markIndic[student_id][course_id] = mark


# List courses

def courseList(course_id):
    print(f"{course_id}: {courseIndic[course_id]['name']}")
        

# List students

def studentList(student_id):
    print(f"+) {student_id}: {studentIndic[student_id]['name']}")
    
# Show student marks for a given course

def displayMark():
    course_id = input("Enter the course ID: ")
    if course_id not in courseIndic:
        print("Course ID is not valid, please type again!")
        return
    for student_id in studentIndic:
        if student_id in markIndic and course_id in markIndic[student_id]:
            print(f"{studentIndic[student_id]['name']}: {markIndic[student_id][course_id]}")
        else:
            print(f"{studentIndic[student_id]['name']}: Not Exist")

# Show both lists of students and courses

def allCourse():
    for course_id in courseIndic:
        courseList(course_id)
        for student_id in studentIndic:
            studentList(student_id)

#Main Function

studentInfo()
courseInfo()


while True:
    print("Pick an option: ")
    print("1. Input marks for a course")
    print("2. Display all course")
    print("3. Display mark list")
    print("4. Quit")
    print("")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        mark()
    elif choice == 2:
        allCourse()
    elif choice == 3:
        displayMark()
    elif choice == 4:
        break
    else:
        print("Corressponding choice not exsit!")

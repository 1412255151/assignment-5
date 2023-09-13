class Student:
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getMarks(self):
        return self.__marks

    def setMarks(self, marks):
        self.__marks = marks

    def addMark(self, mark):
        self.__marks.append(mark)

    def calculateAverage(self):
        if not hasattr(self, '_Student__marks'):
            return 0
        if len(self.__marks) == 0:
            return 0
        return sum(self.__marks) / len(self.__marks)

    def displayStudentInfo(self):
        print(f"Name: {self.__name}")
        print(f"Roll Number: {self.__rollNumber}")
        print(f"Marks: {', '.join(map(str, self.__marks))}")
        print(f"Average Marks: {self.calculateAverage()}")
        
students = []

while True:
    print("\nOptions:")
    print("1. Add a student")
    print("2. View student information")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        student = Student()
        name = input("Enter student's name: ")
        roll_number = input("Enter student's roll number: ")
        student.setName(name)
        student.setRollNumber(roll_number)

        marks = []
        while True:
            try:
                mark = float(input("Enter a mark (or 'done' to finish): "))
                student.addMark(mark)
            except ValueError:
                if input("Invalid input. Do you want to finish entering marks? (yes/no): ").lower() == 'yes':
                    break
                else:
                    continue

        students.append(student)
        print("Student added successfully!")

    elif choice == '2':
        if not students:
            print("No students added yet.")
        else:
            roll_number = input("Enter student's roll number to view information: ")
            found = False
            for student in students:
                if student.getRollNumber() == roll_number:
                    student.displayStudentInfo()
                    found = True
                    break
            if not found:
                print("Student not found.")

    elif choice == '3':
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
def add_students():
    rno = 0
    while rno!=-1:
        rno = int(input("Enter the roll number: "))
        temp_records[rno] = []

def check(x,y):
    if x>y:
        print("Invalid marks!",x,">",y)
        return(1)
    elif x<0:
        print("Invalid marks!",x,"< 0")
        return(1)
    else:
        return(0)

def read_marks():
    rno = int(input("Enter the roll number: "))
    if rno not in temp_records:
        print("Error: Student roll number does not exist")
    else:
        q = int(input("Enter the quiz marks: "))
        if check(q,20)==0:
            temp_records[rno].append(q)
            e = int(input("Enter the exam marks: "))
            if check(e,100)==0:
                temp_records[rno].append(e)
                a = int(input("Enter the assignment marks: "))
                if check(a,100)==0:
                    temp_records[rno].append(a)
                    p = int(input("Enter the project marks: "))
                    if check(p,50)==0:
                        temp_records[rno].append(p)

def compute_gpa():
    rno = int(input("Enter the roll number: "))
    if rno not in temp_records:
        print("Error: Student roll number marks information unavailable")
    else:
        sum = 0
        marks = temp_records[rno]
        percent = (marks[0]*15/20)+(marks[1]*40/100)+(marks[2]*20/100)+(marks[3]*25/50)
        gpa = round(percent/10,2)
        temp_records[rno].append(gpa)
        if gpa == 10:
            grade = 'O'
        elif gpa >= 9:
            grade = 'A'
        elif gpa >= 8:
            grade = 'B'
        elif gpa >= 6.5:
            grade = 'C'
        elif gpa >= 5:
            grade = 'D'
        else:
            grade = 'F'
        temp_records[rno].append(grade)

def generate_records():
    final_records.update(temp_records)

def display_records():
    rno = int(input("Enter the roll number: "))
    if rno not in final_records:
        print("Error: Student roll does not exist")
    else:
        student_details = final_records[rno]
        print("Marks:", student_details[:4])
        print("GPA:", student_details[-2])
        print("Grade:", student_details[-1])
        
print("Menu: \n 1. Add Students \n 2. Read Marks \n 3. Compute GPA and Assign Grade \n 4. Generate Records \n 5. Display Records \n 6. Exit")

temp_records = {}
final_records = {}

opt = 0
while opt!=6:
    opt = int(input("Select one of the tasks from the menu: "))
    if opt == 1:
        add_students()
    elif opt == 2:
        read_marks()
    elif opt == 3:
        compute_gpa()
    elif opt == 4:
        generate_records()
    elif opt == 5:
        display_records()
    elif opt == 6:
        print("Exit")
    else:
        print("Invalid option")

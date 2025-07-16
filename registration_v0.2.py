print("""
┌───────────────────────────────────────────────┐
│         Student Admissoion Register V 0.1     │
├───────────────────────────────────────────────┤
│  Welcome, Admin.                              │
│  Enter The Admission data                     │
│  Assigned the Roll Number and Registration No │
│  To Keep Record and make registration easy    │
├───────────────────────────────────────────────┤
│                                               │
└───────────────────────────────────────────────┘
""")
Section_name = input("Enter the Section of the class: ")
Class_name = input("Enter the Class in Which Students took admission : ")
while True:
    try:
        n = float(input(f"Enter the number of students who took admission in section {Section_name}: "))
        
        # Check if it's a whole number and > 0
        if n <= 0 or n != int(n):
            print("❌ Please enter a valid positive whole number.")
            continue
        
        n = int(n)  # Now safe to convert
        print(f"✔️ The number of students in Class {Class_name} this year is: {n}")
        break

    except ValueError:
        print("❌ Invalid input. Please enter a numeric value.")


while True:
    try:
        roll_number=int(input("Enter the Roll  number Where you would like to start from: "))
        if roll_number <= 0:
            print("❌ Please enter a valid  the roll number.")
            continue
        roll_number  = int(roll_number)  # Now safe to convert
        print(f"✔️ The roll numbers will Start From: {roll_number}")
        break

    except ValueError:
        print("❌ Invalid input. Please enter a Valid roll number.")

while True:
    try:
        reg_number=int(input("Enter the Registration number Where you would like to start from: "))

        if reg_number <= 0 or reg_number != int(reg_number):
            print("❌ Please enter a valid  the roll number.")
            continue
        reg_number  = int(reg_number)  # Now safe to convert
        print(f"✔️ The roll numbers will Start From: {reg_number}")
        break

    except ValueError:
        print("❌ Invalid input. Please enter a Valid roll number.")

   
for _ in range(int(n)):
    name=input("Enter the name of the student: ").strip().title()
    print(f" For student {name} in Section {Section_name} of Class {Class_name} assigned roll number is: {roll_number} and regstration number is : {reg_number}")
    roll_number +=1
    reg_number+=1
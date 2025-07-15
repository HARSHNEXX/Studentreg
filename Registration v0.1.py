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
a=1
b=12130   
for _ in range(int(n)):
    name=input("Enter the name of the student: ").strip().title()
    print(f" For student {name} in Section {Section_name} of Class {Class_name} assigned roll number is: {a} and regstration number is : {b}")
    a+=1
    b+=1
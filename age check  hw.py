def enroll_student(name, age):
    if 10 <= age <= 14:
        print(f"{name} (Age: {age}) has been enrollled successfully")
    else:
        print(f"Sorry {name}, you can't be enrolled. Age{age} is not allowed.")
print("Welcome to Rajs class enrollment system")
students=int(input("Enter the number of students to check "))
for i in range (students):
    name=input(f"\nEnter the name of student {i+1}:")
    age=int(input("Enter the age of {name}"))
enroll_student(name,age)
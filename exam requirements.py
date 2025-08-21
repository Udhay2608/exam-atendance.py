medical_cause=input("Do you have a medical cause yes or no")
attend=int(input("Enter the attendance of the student"))

if medical_cause == "Yes":
    print("You are allowed")
else:
    if attend>=75:
        print("allowed")
    else:
        print("not allowed")

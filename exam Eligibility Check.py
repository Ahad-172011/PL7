medical_cause=input("did you have a medical cause Y or N:")
attendance = int(input("enter the attendance of the student: "))

if medical_cause == 'Y':
    print("You are allowed")
else:
    if attendance>=75:
        print ("allowed")
    else:
        print("Not allowed")
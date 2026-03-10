students = []

quantity_students = int(input("How many students are you going to register?: "))

print("""Welcomeback proffesor to your register system.
    Would you like to start the program?
    (1) Yes.
    (2) No.""")

answer= input("Option to select: ")

if answer == "1":
    for i in range(quantity_students):

        fullname = input(f"Please enter the full name of the student #{i + 1}: ")
        age= input(f"Please enter the age of {fullname}: ")

        students.append({
            "name" : fullname,
            "age"  : age
        })

    print("\n--- Registered Students ---")

    for student in students:
        print(f"The student {student['name']} is {student['age']} years old.")

    print ("\n--- The average in the classroom ---")

    for student in students:
        print(f"The average in age for the classroom of {quantity_students} students is: ")
else:
    print("Option refused, bye.")
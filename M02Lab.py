while(1):
    studentslastname = input("Input Students Last Name: ")
    if studentslastname == "ZZZ":
        break
    else:
        studentsfirstname = input("Input Students First Name: ")
        studentsgpa = float(input("Input Students GPA: "))

        if studentsgpa >= float(3.5):
            print("Student has made the Dean's List.")
        elif studentsgpa >= 3.25:
            print("Student has made the Honor Roll.")
        else:
            print("Student did not make Dean's List or Honor Roll.")
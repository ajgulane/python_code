def computes(module_number):
        def module1():
            user_input = float(input("Enter Value of Radius: "))
            pi = 3.14159256
            Area = pi * (user_input**2)
            Circumference = (2 * pi) * user_input
            Diameter = 2 * user_input
            print("Area is = ",Area,"\nCircumference is = ",Circumference,"\nDiameter is = ",Diameter)

        def module2():
            user_input = int(input("Enter Year: "))
            if user_input % 4 == 0 or user_input % 16 == 0:
                print("Year is a Leap Year")
            else:
                print("Year is not a Leap Year")

        def module3():
            user_input = float(input("Enter Number: "))
            print("The Squared Value is = ", user_input ** 2)
            print("The Cubed Value is = ", user_input ** 3)


        if module_number == '1':
             module1()


        elif module_number == '2':
             module2()


        elif module_number == '3':
            module3()

        else:
            print("Invalid Module Number! Enter 1, 2, or 3.")
        
computes(input("1. Computes area, diameter, and circumference\n2. Identify if year is leap year or not\n3. Computes Square and Cube of a Number\nEnter Module Number: "))



def computes(module_number):
    pi = 3.14159256
    Area = pi * (module_number**2)
    Circumference = 2 * pi * module_number
    Diameter = 2 * module_number

    print("Area is = ",Area,"\nCircumference is = ",Circumference,"\nDiameter is = ",Diameter)

    if module_number % 4 or module_number % 16:
        print("Module Number is a Leap Year")
    else:
        print("Module Number is not a Leap Year")

    print(square = module_number ** 2)
    print(cube = module_number ** 3)
    
computes(float(input("Enter Module Number: ")))



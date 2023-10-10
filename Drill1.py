#Create a program that will let the user choose to get voltage, resistance, and curruents
def drill(userC):
    if userC == 1:
        i = float(input("Enter Currents Value: "))
        r = float(input("Enter Resistance Value: "))
        v = i * r
        print("Voltage(V) is = ", v)
    elif userC == 2:
        v = float(input("Enter Volts Value: "))
        r = float(input("Enter Resistance Value: "))
        i = v / r
        print("Current(A) is = ", i)
    elif userC == 3:
        v = float(input("Enter Volts Value: "))
        i = float(input("Enter Current Value: "))
        r = v * i
        print("Resistance(R) is = ", r)
    else:
        print("invalid value")

drill(int(input("Voltage(V) = 1\nCurrent(A) = 2\nResistance(R) = 3\nChoose Command: ")))

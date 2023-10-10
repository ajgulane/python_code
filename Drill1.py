def calculate_voltage(current, resistance):
    return current * resistance

def calculate_current(voltage, resistance):
    return voltage / resistance

def calculate_resistance(voltage, current):
    return voltage / current

while True:
    print("Choose an option:")
    print("1. Calculate Voltage")
    print("2. Calculate Current")
    print("3. Calculate Resistance")
    print("4. Quit")

    choice = input("Enter your choice 1,2,3,4: ")

    if choice == '1':
        current = float(input("Enter current: "))
        resistance = float(input("Enter resistance: "))
        voltage = calculate_voltage(current, resistance)
        print(f"Voltage is {voltage} V")

    elif choice == '2':
        voltage = float(input("Enter voltage: "))
        resistance = float(input("Enter resistance: "))
        current = calculate_current(voltage, resistance)
        print(f"Current is {current} I")

    elif choice == '3':
        voltage = float(input("Enter voltage: "))
        current = float(input("Enter current: "))
        resistance = calculate_resistance(voltage, current)
        print(f"Resistance is {resistance} ohms")

    elif choice == '4':
        break

    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4)")

def calculate_voltage(current,resistance):
    return current * resistance
def calculate_current(voltage,resistance):
    return voltage/resistance
def calculate_resistance(voltage,current):
    return voltage/current

while True:
    print("Choose an option\n1. Calculate Voltage\n2. Calculate Current\n3. Calculate Resistance\n4. Exit ")
    choice = input("Enter Choice 1/2/3/4: ")
    if choice == '1':
        current = float(input("Enter Current(i): "))
        resistance = float(input("Enter Resistance in Ohms: "))
        voltage = calculate_voltage(current,resistance)
        print(f"The voltage is {voltage} volts")
    elif choice == '2':
        voltage = float(input("Enter Voltage (V): "))
        resistance = float(input("Enter Resistance in Ohms: "))
        current = calculate_current(voltage,resistance)
        print(f"The current is {current} amps")
    elif choice == '3':
        voltage = float(input("Enter Voltage (V): "))
        current = float(input("Enter Current(I): "))
        resistance = calculate_resistance(voltage,current)
        print(f"The resistance is {resistance} R")
    else:
        print("Invalid Choice Please Choose 1/2/3/4")
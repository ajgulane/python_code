WO_1 = float(input("Enter Written Output 1: "))
WO_2 = float(input("Enter Written Output 2: "))
PT_1 = float(input("Enter Performanced Tasks 1: "))
PT_2 = float(input("Enter Performanced Tasks 2: "))

FWO = ((WO_1+WO_2)/2) * 0.6
FPT = ((PT_1+PT_2)/2) * 0.4

Final_Grade = FWO + FPT
print("The Final Grade is: ", Final_Grade)
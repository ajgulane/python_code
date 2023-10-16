#Create a program that takes a numeric grade as input and outputs 
#the corresponding letter grade (A, B, C, D, or F) 
#based on the following scale:
#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59
while True:
    def GradeCalculator(grade):
        if grade >= 90 and grade <= 100:
            return 'A'
        elif grade >= 80:
            return 'B'
        elif grade >= 70:
            return 'C'
        elif grade >= 60:
            return 'D'
        elif grade >= 0:
            return 'F'
    
    print(GradeCalculator(float(input("Enter Grade: "))))
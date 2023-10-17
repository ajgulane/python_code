def isCon():
    x = input("Enter Letter: ").lower()
    vowel = ['a','e','i','o','u']

    if x in vowel:
        print("is Vowel")
    else:
        print("is Consonant")
    
def isOdd():
    user_input = int(input("Enter Number: "))

    if user_input % 2 == 0:
        print("is Even")
    else:
        print("is Odd")

user_input = input("Enter A/a or B/b: ").lower()

if user_input == 'a':
    isCon()

elif user_input == 'b':
    isOdd()

else:
    print("Invalid Input")

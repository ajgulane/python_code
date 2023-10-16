while True:
    try:
        x, y = input("Enter Two Number: ").split()

        print('this is x', x)
        print('this is y', y) 
        print('average is ', (int(x) + int(y))/2)
    except:
        print('Invalid Please Enter Two Numbers\nEx.10 5')
     
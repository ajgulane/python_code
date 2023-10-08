def identify(x):
    try:
        int(x)
        print("Integer")
    except:
        try:
            float(x)
            print("Float")
        except:
            print("String")

identify(input("Enter Value: "))
    
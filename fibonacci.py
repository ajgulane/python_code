a = 0
b = 1
c = 0
fibonacci = [0]

n = int(input("Enter N: "))
for i in range(n):
    c = a + b
    fibonacci.append(c)

    b = a
    a = c
print(fibonacci)


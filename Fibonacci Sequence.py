# Fibonacci Sequence

a = 0 #1 
b = 1 #1
Fibonacci = [a, b]
for sayilar in range(1, 21):
    a, b = b, a + b
    Fibonacci.append(b)

print(Fibonacci)
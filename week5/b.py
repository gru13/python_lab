def bitwise_addition(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1  # Shift carry to the left by 1
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = bitwise_addition(num1, num2)
print("Bitwise addition:", result)

a = 1
b = 2

carry = 0

a = str(bin(a))[2:][::-1]
b = str(bin(b))[2:][::-1]

result = ""

while not(len(a) and len(b)):
    i = int(a.pop(0)) 
    j = int(a.pop(0)) 

    sum_ = i ^ j 
    carry = i & 
print(a,b)
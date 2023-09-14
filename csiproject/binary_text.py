#Working with binary and hex values
'''
x1 = 0b111111 #The 0b indicates that this is a binary value
x2 = 0b1111111
x3 = x2 - x1
x3 = bin(x3)
x4 = x1 - x2
#print(x3)
#print(x4)
x4 = bin(x4)
#print(x4)

y1 = 0xfff #For hex values, prefix with 0x
print(y1)
y2 = hex(567)
print(y2)
y3 = 0x1ea
print("y3 equals",y3)
result = y1 + y3
print(result)
result2 = y3 - y1
result2 = hex(result2)
print(result2)
'''

a = 0b101010
b = 0b111110

a_b = a - b

print("The binary result of",bin(a),"-",bin(b),"equals",bin(a_b))
print("The base 10 result of",bin(a),"-",bin(b),"equals",a_b)
print("The hexadecimal result of",bin(a),"-",bin(b),"equals",hex(a_b))

mul2 = []
mul3 = []
mul6 = []
others = 0

for i in range(1, 101):
    if i%6 == 0:
        mul6.append(i)
    elif i%3 == 0:
        mul3.append(i)
    elif i%2 == 0:
        mul2.append(i)
    else:
        others += i

print("mul2 : ", mul2)
print("mul3 : ", mul3)
print("mul6 : ", mul6)
print("others: ", others)

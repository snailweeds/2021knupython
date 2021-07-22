mul2 = []
mul3 = []
mul6 = []
others = 0

for i in range(1, 100):
    if i%2 == 0:
        mul2.append(i)
    elif i%3 == 0:
        mul3.append(i)
    elif i%6 == 0:
        mul6.append(i)
others += i

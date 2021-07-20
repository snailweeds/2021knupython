name = "홍길동"
age = 25
height = 184.6
print(type(name))
print(type(age))
print(type(height))

# Convention, 파이썬 PEP-8
"""
1. 한 단어로 된 변수는 소문자로 작성 (age, good, name)
2. 두 단어 이상의 변수는 언더바로 구분 (my_name, my_friend_name)
3. 예약어와 충돌하는 경우에는 뒤에 언더바 덧붙이기 (if_, time_)
4. 상수의 경우 대문자와 언더바 혼용하여 사용 (TOTAL, MAX_NUM, AVG)
"""

# number_datatypes
a = 154
print(type(a))
a = 0
print(type(a))
a = -25
print(type(a))

b = 181.34
print(type(b))
b = -22.22
print(type(b))

c = 1 + 4j
print(type(c))
print(c.real)
print(c.imag)
print(c.conjugate())
print(abs(c))

# Example
aa = 5
bb = 3.14
cc = 3 + 4j
print(10*aa + 3*bb + cc)

# bool_datatypes
abo = True
bbo = False
print(type(abo), type(bbo))

x = 1
y = 2
print(x>y)
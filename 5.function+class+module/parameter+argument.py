def add_two_num(a=100, b=200):
    print("더하는 중...")
    print(a, b)
    result = a + b # 지역변수 result
    return result # 함수 결과값

#value = add_two_num(a=10 , b=13)
value1 = add_two_num(10, 13)
value2 = add_two_num(10)
value3 = add_two_num(b = 10)
value4 = add_two_num()
print(value1, value2, value3, value4)
'''
def add_two_num(a=100, b) # 불가능
...
def add_two_num(a, b=100) # 가능
...
''' 
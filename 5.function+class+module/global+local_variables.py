def add_two_num(a, b):
    print("더하는 중...")
    result = a + b # 지역변수 result
    return result

result = 0 # 전역변수 result
value = add_two_num(100, 13)
print(value)
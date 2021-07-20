s2 = "Hello Haedal!"
print(s2)

s6 = '''Hello Haedal!'''
print(s6)

# 이스케이프 코드
longtext1 = """Hello, Haedal!
My name is Haedal Programmiing.""" # 개행 가능
print(longtext1)

longtext2 = 'Hello, Haedal!\nMy name is Haedal Programmiing.' # 개행 불가능
print(longtext2)

# String Interpolation
a = 123
new_q = f'{a}'
print(new_q)

# 문자열 옛날 방식
print(f'%s %s' % ('one', 'two'))

# pyformat
print('{} {}'.format('one', 'two'))

# f-string
aa, bb = 'one', 'two'
print(f'{aa} {bb}')
print(f'{bb} {aa}')

name = '해달'
eng_name = 'Haedal'
print(f"안녕하세요. {name}입니다. My name is {eng_name}")
print("안녕하세요. {1}입니다. My name is {0}".format(eng_name, name))

# 문자열 인덱싱
a = "Hello, Haedal!"
print(a[1])

# 문자열 슬라이싱
print(a[4:9])

# 문자열 길이
print(len(a))

am = '312'
bm = 'bac'
print(min(am))
print(max(am))
print(min(bm))
print(max(bm))
print(am+bm)
print(min(am+bm))
print(max(am+bm))

# 소문자, 대문자로 변환
ac = "This is Apple"
print(ac.upper())
print(ac.lower()) 

# 문자열 구분자에 따라 나누기
a = "안녕,나는,해달이야"
print(a.split(sep=","))
b = "안녕 나는 해달이야"
print(b.split())

# 여러 개의 문자열 사이에 구분자 넣어주기
lister = ['안녕', '나는', '해달']
stringer = "_".join(lister)
print(stringer)
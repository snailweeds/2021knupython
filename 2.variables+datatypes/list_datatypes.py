Haedal_character = ["해달이", "시라용", "아리", "메기", "사스미"]
mylist = []
print(mylist)

mylist = [1, 2, "해달이", True, ['a', 'b', 'c']]
print(mylist)

# 리스트 인덱싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[0])
print(a[5])
print(a[9])
print(a[-1])
print(a[-5])

# 리스트 슬라이싱
print(a[0:3])
print(a[1:3])
print(a[:3])
print(a[7:])
print(a[:])
print(a[-4:-2])

# 리스트 수정
a[0] = 100
print(a)

del a[0]
print(a)

del a[3:]
print(a)

a = [1,2,3,4]
print(len(a))
mylist = ['a', 'b', 'c', 'd']
mylist.append('e')
print(mylist)

# 리스트 정렬
num = [4, 2, 3, 1]
num.sort()
print(num)

num.sort(reverse=True)
print(num)
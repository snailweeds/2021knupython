for i in range(1, 11):
    if (i%2==0):
        print(i, "은/는 짝수입니다.")
    else:
        print(i, "은/는 홀수입니다.")

# for문의 구조
"""
for i in 범위:
    반복할 명령어1
    반복할 명령어2
"""

# for문 with list
mylist = ['해달이', '메기', '고구마']
for i in mylist:
    print(i)
print("반복 끝!")

# print list with range
print(list(range(1, 11)))
print(list(range(1, 20, 3)))
print(list(range(20, 0, -3)))

# for문 with range
for i in range(1, 11):
    print(i, end=" ")
print("반복 끝!")
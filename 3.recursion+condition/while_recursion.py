# for문은 정해진 횟수만큼, while은 정해진 목표까지
it = 0
while it<5:
    it += 1
    print(it)

# while문 구조
"""
while 조건:
    반복할 명령어1
    반복할 명령어2
"""

# while 무한루프
# it = 0
# while True:
#     it += 1
#     print(it)

# while 무한루프 + break
it = 0
while True:
    it += 1
    print(it)
    if it > 500:
        break


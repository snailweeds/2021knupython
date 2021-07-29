# 클래스 - 붕어빵 틀 만들기
class FishBread:
    # 붕어빵 굽기
    def __init__(self, ingredients, price):
        self.__ingredients = ingredients
        self.__price = price
    # 붕어빵 살펴보기
    def __str__(self):
        return '{}붕어빵, 가격 {}원'.format(self.__ingredients, self.__price)

    def __add__(self, other):
        return self.__price + other.__price

# 인스턴스=객체 만들기
a = FishBread("팥", 400)
b = FishBread("슈크림", 500)

print(a)
print(b)

print("붕어빵 a, b 합쳐 %d원" % (a+b))
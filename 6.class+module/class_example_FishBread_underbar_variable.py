# 클래스 - 붕어빵 틀 만들기
# __ 언더바를 추가하면 접근 권한이 없어져 수정 불가
class FishBread:
    banjook = "밀가루"
    # 붕어빵 굽기
    def make_FB(self, ingredients, price):
        self.__ingredients = ingredients
        self.__price = price
    # 붕어빵 살펴보기
    def see_FB(self):
        print(self.__ingredients, self.__price)

# 인스턴스=객체 만들기
a = FishBread()
a.make_FB("팥", 400)
print(a.__ingredients, a.__price)
a.price = 10
a.see_FB()